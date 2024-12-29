from .models import Post, Profile
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import (
    LoginForm,
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm,
    PostForm,
)
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.forms import ClearableFileInput
from django.shortcuts import redirect


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "gallery/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "gallery/detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset or self.get_queryset()
        return get_object_or_404(queryset, **{self.slug_field: slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        context["preview"] = self.object.preview
        context["body"] = self.object.body
        context["publish"] = self.object.publish
        context["image"] = self.object.image
        return context


class OwnerMixin:
    """Mixin для фильтрации объектов по автору."""

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class OwnerEditMixin:
    """Mixin для установки текущего пользователя как автора."""

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Класс для проверки владельца статьи
class OwnerPostMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user


# Список статей
class ManagePostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "gallery/dashboard.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


# Создание статьи
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "gallery/create-update.html"
    success_url = "/"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем автора
        return super().form_valid(form)


# Обновление статьи
class PostUpdateView(LoginRequiredMixin, OwnerPostMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "gallery/create-update.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()  # Передаем объект в контекст
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем автора
        return super().form_valid(form)


# Удаление статьи
class PostDeleteView(LoginRequiredMixin, OwnerPostMixin, DeleteView):
    model = Post
    template_name = "gallery/delete.html"
    success_url = "/"


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Создаем объект пользователя, но не сохраняем его сразу
            new_user = user_form.save(commit=False)
            # Устанавливаем пароль
            new_user.set_password(user_form.cleaned_data["password"])
            # Сохраняем пользователя в базе данных
            new_user.save()
            print(f"Пользователь создан: {new_user.username}")

            # Создаем профиль для нового пользователя
            profile = Profile.objects.create(user=new_user)
            print(f"Создан профиль для пользователя: {new_user.username}")

            # Аутентификация пользователя
            user = authenticate(
                username=new_user.username, password=user_form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)  # Вход в систему
                print(f"User  {user.username} успешно вошел")

                # Перенаправляем на страницу dashboard
                return redirect("/")
            else:
                print("Вход не был выполнен: Неверен username или password.")
        else:
            print("User  registration form is not valid.")
            print(user_form.errors)  # Вывод ошибок формы
    else:
        user_form = UserRegistrationForm()

    return render(request, "gallery/register.html", {"user_form": user_form})


from django.contrib.auth.models import User
from django.http import HttpResponseNotFound


@login_required
def dashboard(request, username=None):
    # Получаем пользователя: либо по username, либо текущего авторизованного
    user = get_object_or_404(User, username=username) if username else request.user

    # Получаем профиль пользователя, если он существует
    profile = Profile.objects.filter(
        user=user
    ).first()  # Возвращает None, если профиль не найден

    # Получаем статьи, автором которых является текущий пользователь
    posts = Post.objects.filter(author=user)

    # Отображаем страницу с данными пользователя, профиля и статей
    return render(
        request,
        "gallery/dashboard.html",
        {"user": user, "profile": profile, "posts": posts},
    )


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("edit")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "gallery/edit.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "username": request.user.username,
        },
    )
