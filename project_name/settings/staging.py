# Settings for staging

from .gae import *

DEBUG = False

DATABASES['default']['name'] = '{{ project_name }}_staging'