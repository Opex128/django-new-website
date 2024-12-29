from django.contrib import admin
from .models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish"]
    list_filter = ["created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "photo", "date_registr"]
    raw_id_fields = ["user"]
