"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l(-6h(a%(l9vrqh$-@gd$2_h(b56!u#an$g9+17h+vpd^y*j=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # app
    'apiv1.apps.Apiv1Config',
    'woop.apps.WoopConfig',
    'accounts',


    # 3rd party
    'corsheaders',
    'rest_framework',
    'django_js_reverse',
    'silk',
    'drf_yasg',
    'django_extensions',

    # 認証,　認可
    'djoser',
    'rest_auth',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
]


### for allauth
SITE_ID=1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Eliminate the need for an SMTP server
# ref : https://stackoverflow.com/questions/21563227/django-allauth-example-errno-61-connection-refused
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Tells rest_auth to use a custom user serializer instead of the default user serializer.
REST_AUTH_SERIALIZERS = {
         # http://localhost:8000/rest-auth/user/
         # ref : https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
        'USER_DETAILS_SERIALIZER': 'apiv1.serializers.CustomUserSerializer',
}



AUTH_USER_MODEL = 'accounts.CustomUser'

# Django REST frameworkの設定
REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'

}

SIMPLE_JWT = {
    # Change default `USER_ID_FIELD` to `id` of CustomUser.
    'USER_ID_FIELD': 'user_id',
    'JWT_ALLOW_REFRESH': True,
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24)
}

SESSION_COOKIE_HTTPONLY = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 3rd party
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'silk.middleware.SilkyMiddleware',
]

# CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_NAME = "csrftoken"

CORS_ORIGIN_WHITELIST = [
    'https://fiddle.jshell.net',
    'http://127.0.0.1:5500',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'http://192.168.3.7:8080',
    'http://192.168.3.7:8080',
    'http://192.168.129.16:8080',
    'http://192.168.3.6:8080',
    'http://192.168.129.16:8080',
    'http://10.4.102.65:8080',
    'http://10.4.102.103:8080',

]

ROOT_URLCONF = 'config.urls'


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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

if DEBUG:
    def show_toolbar(request):
        return True
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar}
