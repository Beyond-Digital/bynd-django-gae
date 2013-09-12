# Import common settings from base
from .base import *

# Take namespace from appengine config - local, dev, qa, staging, live
from appengine_config import namespace as env

# Import settings from env-specific file
import importlib
import sys

# Bring vars from env-specific settings file into scope
curr_module = sys.modules[__name__]
env_settings = importlib.import_module('.%s' % env, package=__package__)

for var, value in vars(env_settings).iteritems():
    setattr(curr_module, var, value)
