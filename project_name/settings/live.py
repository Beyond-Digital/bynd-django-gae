# Settings for live - eg DEBUG = False

from .gae import *

DATABASES['default']['name'] = '{{ project_name }}_live'