"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import json
from celery.schedules import crontab
from celery import app
from environs import Env
import sys 
from corsheaders.defaults import default_headers
from datetime import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

E_VARS = json.loads(os.environ["ENV_CONFIG"])

ENV_VARS = { key: value for (key, value) in ( { **E_VARS }.items() ) }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bn(9*+wn89l@!@jg+@m76n-abvwcz=vaf5-0bn@+3(#d(u)*ka'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
START_TIME = datetime.strptime(ENV_VARS['START_TIME'],"%H:%M")
END_TIME = datetime.strptime(ENV_VARS['END_TIME'],"%H:%M")
STRING_MATCH = ENV_VARS['STRING_MATCH']
MESSAGE_LENGTH =  ENV_VARS['LENGTH']
KEYWORDS = ENV_VARS['KEYWORDS']
SEND_LIMIT = ENV_VARS['SEND_LIMIT']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conversation',
    'user',
    'store'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': ENV_VARS['DATABASE_NAME'],
        'USER': ENV_VARS['DATABASE_USER'],
        'PASSWORD': ENV_VARS['DATABASE_PASSWORD'],
        'HOST': ENV_VARS['DATABASE_HOST'],
        'PORT': ENV_VARS['DATABASE_PORT'],
    }
}

CELERY_BROKER_URL = ENV_VARS['CELERY_REDIS_URL']
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_RESULT_BACKEND = ENV_VARS['CELERY_REDIS_URL']
CELERY_TRACK_STARTED = True
CELERY_BEAT_SCHEDULE = {
    'send_notication-every-1-hours': {
       'task': 'conversation.tasks.send_notication',
       'schedule': crontab(minute=0, hour='*/1'),
       'options': {'queue' : 'high_priority'}
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ENV_VARS['EMAIL_HOST']
EMAIL_PORT = ENV_VARS['EMAIL_PORT']
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ENV_VARS['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = ENV_VARS['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True