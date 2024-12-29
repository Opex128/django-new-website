from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-66d=eq%8l6%!plz32$ojl124#e3rd3wbpq^23xd5o1c2ia0skw"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "crispy_forms",
    "crispy_bootstrap4",
    "gallery.apps.GalleryConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_ckeditor_5",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

CKEDITOR_UPLOAD_PATH = "images/"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "mysite2.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

import os

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "/"

CKEDITOR_5_CUSTOM_CSS = "css/gallery.css"
customColorPalette = [
    {"color": "hsl(0, 100%, 50%)", "label": "Красный"},  # Изменено на чистый красный
    {"color": "hsl(300, 100%, 50%)", "label": "Розовый"},  # Изменено на чистый розовый
    {"color": "hsl(240, 100%, 50%)", "label": "Синий"},  # Изменено на чистый синий
    {"color": "hsl(120, 100%, 50%)", "label": "Зеленый"},  # Добавлен зеленый
    {"color": "hsl(60, 100%, 50%)", "label": "Желтый"},  # Добавлен желтый
    {"color": "hsl(30, 100%, 50%)", "label": "Оранжевый"},  # Добавлен оранжевый
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "undo",
            "redo",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "bold",
            "italic",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "link",
            "imageUpload",
        ],
    },
    "extends": {
        "toolbar": [
            "undo",
            "redo",
            "|",
            "fontSize",
            "fontFamily",
            "bold",
            "italic",
            "|",
            "removeFormat",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "link",
            "imageUpload",
            "|",
            "horizontalLine",
        ],
        "removePlugins": ["WordCount"],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
            ],
        },
        "fontSize": {"options": [i for i in range(10, 26, 2)]},
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Параграф",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Заголовок 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Заголовок 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Заголовок 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
    },
}
