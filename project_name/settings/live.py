# Settings for live - eg DEBUG = False

from .gae import *

DEBUG = False

DATABASES['default']['NAME'] = '{{ project_name }}_live'