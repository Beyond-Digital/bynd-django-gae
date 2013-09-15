# Settings for testing

from .gae import *

DEBUG = True

DATABASES['default']['name'] = '{{ project_name }}_testing'