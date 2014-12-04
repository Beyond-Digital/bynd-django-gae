"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

import django.conf.global_settings as default_settings

BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
)

# Add lib folder
sys.path.append(os.path.join(BASE_DIR, 'vendor'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# Application definition
INSTALLED_APPS = (

    # Contrib apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Vendor apps
    'djangosecure',

    # Project apps
    '{{ project_name }}'
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'google.appengine.ext.ndb.django_middleware.NdbDjangoMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'gaekit.caches.GAEMemcachedCache',
        'TIMEOUT': 0,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
DEFAULT_FILE_STORAGE = 'gaekit.storages.CloudStorage'
GS_BUCKET_NAME = '{{ project_name }}'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Use cookie session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# Security settings
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
