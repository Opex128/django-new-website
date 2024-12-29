from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

import random
from pytils.translit import slugify


# Статьи
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


def generate_unique_slug(klass, title):
    # Генерируем базовый slug из title
    base_slug = slugify(title)
    unique_slug = base_slug
    numb = 1
    # Проверяем, существует ли slug в базе данных
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{numb}"  # Добавляем числовой суффикс
        numb += 1
    return unique_slug


from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)  # Уникальный slug
    preview = models.TextField(null=True)
    body = CKEditor5Field(config_name="extends")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gallery_posts"
    )
    link = models.URLField(max_length=150, blank=True, null=True)

    objects = models.Manager()  # менеджер, применяемый по умолчанию

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.title:
            raise ValueError("Title must not be empty to generate a slug.")

        # Преобразование title в slug-формат
        slugified_title = slugify(self.title)  # Преобразуем title в slug-формат

        # Если slug не установлен, генерируем его
        if not self.slug:
            random_number = random.randint(100, 999)
            self.slug = f"{random_number}-{slugified_title}"

            # Проверка уникальности slug
            while Post.objects.filter(slug=self.slug).exists():
                random_number = random.randint(
                    100, 999
                )  # Генерируем новый уникальный идентификатор
            self.slug = f"{random_number}-{slugified_title}"  # Формируем новый slug

        super().save(*args, **kwargs)  # Сохраняем объект


from django.utils import timezone


# Профиль пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # blank=True поле необязательное и его можно оставить пустым
    date_registr = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(
        upload_to="images", verbose_name="Фотография", blank=True, null=True
    )

    def __str__(self):
        return f"Profile of {self.user.username}"
