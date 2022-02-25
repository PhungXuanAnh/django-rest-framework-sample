"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

import environ

env = environ.Env()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "8khss#nb@$*(blml2q@jwvaz!ehxq8qtq29=49!vhf3ck1r)9r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=True)

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    # default see here: https://www.django-rest-framework.org/api-guide/settings/
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    "PAGE_SIZE": 10,
    # "DEFAULT_AUTHENTICATION_CLASSES": [
    #     "cantec_delivery.cd_base.utility.CustomJWTAuthentication",
    # ]
    # "DEFAULT_PERMISSION_CLASSES": [],
    "UNAUTHENTICATED_USER": None,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    # pylint: disable=line-too-long
    # "EXCEPTION_HANDLER": "cantec_delivery.cd_base.utility.drf_exception_handler.custom_exception_handler",
    # "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%fZ",
    # "DEFAULT_THROTTLE_CLASSES": [
    #     "cantec_delivery.cd_base.utility.throttling_request.CustomUserRateThrottle",
    #     "cantec_delivery.cd_base.utility.throttling_request.AnonymousRateThrottle",
    # ],
    # "DEFAULT_THROTTLE_RATES": {"anonymous": "20/second", "custom_user": "20/second"},
    # "ORDERING_PARAM": "sort",
}

# Application definition

INSTALLED_APPS = [
    "system_app",  # this app for test overwrite runserver command
    "admin_numeric_filter",
    "django.contrib.admin",
    "rangefilter",  # for admin filter data/datetime range
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "drf_yasg",
    "user",
    "music",
]

MIDDLEWARE = [
    "main.middlewares.logging.LoggingMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

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

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB", default="xuananh_db"),
        "USER": env("POSTGRES_USER", default="postgres"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="123456"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("POSTGRES_PORT", default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# url for static file, ex: for admin app, it will be http://localhost:8027/static/admin
# then static files wil be file in ../static_files/admin folder as config at STATIC_ROOT below
STATIC_URL = "/static/"
# all static file will be copied here when run python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")


LOGGING_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)
LOGGING_FORMATTER = {
    "verbose": {
        # pylint: disable=line-too-long
        "format": "[%(asctime)s] [%(name)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s"
    },
    "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
}
LOGGING_ROTATING_FILE_HANDLER_SETTINGS = {
    "class": "logging.handlers.RotatingFileHandler",
    "formatter": "verbose",
    "mode": "a",
    "maxBytes": 50 * 1024 * 1024,  # 50M
    "backupCount": 3,
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": LOGGING_FORMATTER,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "requests.FILE": {
            "filename": LOGGING_DIR + "/requests.log",
            **LOGGING_ROTATING_FILE_HANDLER_SETTINGS,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "apps": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "requests": {
            "handlers": ["console", "requests.FILE"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda _: DEBUG,
    }

# ============================= init sentry ================================================
# pylint: disable=wrong-import-position
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SENTRY_DSN = env(
    "SENTRY_DSN", default=""
)  # NOTE: if not set SENTRY_DSN sentry will be disabled

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
