# Settings for staging

from .gae import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'bynd.com:bynd_testing:bynd_testing',
        'NAME': '{{ project_name }}_staging'
    }
}

ALLOWED_HOSTS = ['staging-dot-{{ project_name }}.appspot.com']
