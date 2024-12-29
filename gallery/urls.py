from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views


urlpatterns = [
    # Главная страница
    path("", views.PostListView.as_view(), name="post_list"),
    # Страница пользователя
    path(
        "dashboard/<str:username>/",
        views.dashboard,
        name="dashboard",
    ),
    # Подробная информация о статье
    path(
        "post/<slug:slug>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    # вход
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # выход
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # регистарция
    path("register/", views.register, name="register"),
    # Редактирование профиля
    path("edit/", views.edit, name="edit"),
    # Удаление статьи
    path(
        "post/<slug:slug>/delete",
        views.PostDeleteView.as_view(),
        name="delete",
    ),
    # Создание статьи
    path(
        "create/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
    # Обновление статьи
    path(
        "post/<slug:slug>/update_post",
        views.PostUpdateView.as_view(),
        name="update_post",
    ),
]
