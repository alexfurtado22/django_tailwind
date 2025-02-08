"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x-j-(3ey1g091!igcj%krah5t=#0@z76a(_--7m=k#%jhz^%g%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS = ["allauth.account.auth_backends.AuthenticationBackend"]


# Application definition

# apps.py (or installed_apps.py)
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "tailwind",
    "django_browser_reload",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",  # Example for social login
    "allauth.socialaccount.providers.github",  # Example for social login
    "widget_tweaks",
]

PROJECT_APPS = [
    "app.apps.AppConfig",
    "theme",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

if DEBUG:
    # Add Django Debug Toolbar to installed apps only in development
    INSTALLED_APPS += ["debug_toolbar"]

    # Add the Debug Toolbar middleware to the middleware stack
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    import socket

    # Get the hostname and associated IP addresses
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())

    # Generate Docker internal network IPs (assuming a standard Docker network setup)
    docker_ip = [ip[:-1] + "1" for ip in ips]

    # Define internal IPs to allow access to the Debug Toolbar
    # This includes localhost (127.0.0.1) and dynamically detected internal IPs
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]

    # Configure the Debug Toolbar to only be shown in development and for internal IPs
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG
        and request.META.get("REMOTE_ADDR", "") in INTERNAL_IPS,
    }


ROOT_URLCONF = "myproject.urls"

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

WSGI_APPLICATION = "myproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env.local"))  # Load .env.local file

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # Use PostgreSQL if DATABASE_URL is set
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    # Directly set up PostgreSQL for local development
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "mydatabase",  # Your PostgreSQL database name
            "USER": "myuser",  # Your PostgreSQL username
            "PASSWORD": "lp874dpudc22",  # Your PostgreSQL password
            "HOST": "localhost",  # PostgreSQL server address
            "PORT": "5432",  # PostgreSQL default port
        }
    }


# Customer user model
AUTH_USER_MODEL = "app.UserProfile"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "account_login"

# Allauth settingss
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# URL for accessing uploaded media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# URL to access static files
STATIC_URL = "/static/"

# Directory where collected static files will be stored for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# Additional directories to look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "theme/static",  # Points to 'static'
    BASE_DIR / "theme/static_src/src",  # Points to 'src'
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
