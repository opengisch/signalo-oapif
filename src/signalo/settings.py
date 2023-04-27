"""
Django settings for signalo project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "django"]


# Application definition

INSTALLED_APPS = [
    "signalo.edge_cases",
    "signalo.value_lists",
    "signalo.core",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "rest_framework",
    "rest_framework_gis",
    "computedfields",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "signalo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "signalo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "postgres",
        "HOST": "postgres",
        "PORT": 5432,
        "USER": "postgres",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", BASE_DIR.joinpath("static"))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", BASE_DIR.joinpath("media"))


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
REST_FRAMEWORK = {
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    # "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    # "rest_framework.authentication.SessionAuthentication",
    # "geocity.auth.InternalTokenAuthentication",
    # ),
    "DEFAULT_PAGINATION_CLASS": "django_oapif.pagination.OapifPagination",
    # "DEFAULT_THROTTLE_CLASSES": [
    #     "rest_framework.throttling.ScopedRateThrottle",
    # ],
    # "DEFAULT_THROTTLE_RATES": {
    #     # Full API for permits
    #     "permits": os.getenv("DRF_THROTTLE_RATE_PERMITS_API"),
    #     # Full API for permits_details
    #     "permits_details": os.getenv("DRF_THROTTLE_RATE_PERMITS_DETAILS_API"),
    #     # Limited pulic API used mainly by Geocalendar front app
    #     "events": os.getenv("DRF_THROTTLE_RATE_EVENTS_API"),
    #     # Full API for search
    #     "search": os.getenv("DRF_THROTTLE_RATE_SEARCH_API"),
    # },
    # TODO: remove in favor of whatever ends up in https://github.com/opengisch/signalo-oapif/pull/29
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}

OAPIF_TITLE = "SIGNALO_ROADSIGNS_OAPIF"
OAPIF_DESCRIPTION = "SIGNALO_ROADSIGNS_OAPIF"

# Geometry's SRID. This can only be changed prior to initializing the database.
GEOMETRY_SRID = int(os.environ.get("GEOMETRY_SRID", "2056"))

INTERNAL_IPS = [
    "127.0.0.1",  # so that Django toolbar is displayed to localhost
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
