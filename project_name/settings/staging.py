# Settings for staging

from .gae import *

DEBUG = False

DATABASES['default']['NAME'] = '{{ project_name }}_staging'