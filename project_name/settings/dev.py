# Settings for dev

from .gae import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'bynd.com:bynd_testing:bynd_testing',
        'NAME': '{{ project_name }}_dev'
    }
}
