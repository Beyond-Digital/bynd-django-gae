# Settings for live - eg DEBUG = False

from .gae import *

DEBUG = False

DATABASES['default']['name'] = '{{ project_name }}_live'