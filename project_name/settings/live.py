# Settings for live - eg DEBUG = False

from .gae import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'bynd.com:bynd_testing:bynd_testing',
        'NAME': '{{ project_name }}_live'
    }
}

ALLOWED_HOSTS = ['{{ project_name }}.appspot.com']
