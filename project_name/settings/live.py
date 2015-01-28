# Settings for live - eg DEBUG = False

from .gae import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/bynd.com:{{ project_name }}:{{ project_name }}',
        'NAME': '{{ project_name }}_testing',
        'USER': 'root',
    }
}

ALLOWED_HOSTS = ['{{ project_name }}.appspot.com']
