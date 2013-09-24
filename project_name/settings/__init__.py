# Import common settings from base
from .base import *

# Take namespace from appengine config - local, dev, testing, staging, live
from appengine_config import namespace as env

# Import settings from env-specific file
import importlib
import sys

# Bring vars from env-specific settings file into scope
IMP = vars(importlib.import_module('.%s' % env, package=__package__))

for var, value in IMP.iteritems():
    setattr(sys.modules[__name__], var, value)
