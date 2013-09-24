# Settings for testing

from .gae import *

DEBUG = True

DATABASES['default']['NAME'] = '{{ project_name }}_testing'
