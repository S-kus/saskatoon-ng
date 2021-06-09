"""
Django settings for saskatoon project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/

To set new settings, adapt the following ``.env``
file and place it inside ``saskatoon/`` project directory.

::

    # SECURITY WARNING: keep the secret key used in production secret!
    # More infos: https://docs.djangoproject.com/fr/3.1/ref/settings/#secret-key
    SASKATOON_SECRET_KEY='<KEY>'

    # SECURITY WARNING: don't run with debug turned on in production!
    SASKATOON_DEBUG=no

    # Database settings
    SASKATOON_DB_ENGINE=django.db.backends.mysql
    SASKATOON_DB_NAME=saskatoon_prod
    SASKATOON_DB_USER=saskatoon
    SASKATOON_DB_PASSWORD=
    SASKATOON_DB_HOST=127.0.0.1

    # Misc
    SASKATOON_TIME_ZONE=UTC

"""

import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv #type: ignore

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the environment variables from .env file.
file = find_dotenv(raise_error_if_not_found=True)
if file: load_dotenv(dotenv_path=file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SASKATOON_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('SASKATOON_DEBUG') is not None:
    DEBUG = os.getenv('SASKATOON_DEBUG', '').lower() in ['yes', 'true']
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

# needed by debug toolbar
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'leaflet',
    'sitebase',
    'member',
    'harvest',
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'saskatoon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'saskatoon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SASKATOON_DB_ENGINE'),
        'NAME': os.getenv('SASKATOON_DB_NAME'),
        'USER': os.getenv('SASKATOON_DB_USER'),
        'PASSWORD': os.getenv('SASKATOON_DB_PASSWORD'),
        'HOST': os.getenv('SASKATOON_DB_HOST'),
    }
}

# Remove WARNINGS due to changes in Django3.2 where the type for primary keys can
# now be customized (set by default to BigAutoField starting in Django 3.2):
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('fr',u'Français'),
    ('en',u'English'),
]

LOCALE_PATHS = [
    'harvest/locale/',
    'member/locale/',
    'sitebase/locale/',
    'saskatoon/locale/'
]

CSRF_COOKIE_SECURE = True

TIME_ZONE = os.getenv('SASKATOON_TIME_ZONE') or 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


# EMAIL SERVER (TODO)
DEFAULT_FROM_EMAIL = os.getenv('SASKATOON_FROM_EMAIL')
EMAIL_HOST_USER = os.getenv('SASKATOON_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('SASKATOON_EMAIL_HOST_PASSWORD')
SEND_MAIL_FAIL_SILENTLY = not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD


# CUSTOM STUFF

AUTH_USER_MODEL = "member.AuthUser"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   'PAGINATE_BY': 10,
   'DEFAULT_RENDERER_CLASSES': (
   'rest_framework.renderers.TemplateHTMLRenderer',
   'rest_framework.renderers.JSONRenderer',
)
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
