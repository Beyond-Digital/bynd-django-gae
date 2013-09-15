# Settings for dev

from .gae import *

DEBUG = True

DATABASES['default']['name'] = '{{ project_name }}_dev'