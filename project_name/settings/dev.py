# Settings for dev

from .gae import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/bynd.com:{{ project_name }}:{{ project_name }}',
        'NAME': '{{ project_name }}_testing',
        'USER': 'root',
    }
}

ALLOWED_HOSTS = ['dev-dot-{{ project_name }}.appspot.com']
