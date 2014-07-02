# Settings for testing

from .gae import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'bynd.com:bynd_testing:bynd_testing',
        'NAME': '{{ project_name }}_testing'
    }
}

ALLOWED_HOSTS = ['testing-dot-{{ project_name }}.appspot.com']
