# Settings for dev

from .gae import *

DEBUG = True

DATABASES['default']['NAME'] = '{{ project_name }}_dev'