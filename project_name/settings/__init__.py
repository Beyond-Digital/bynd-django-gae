from .base import *

# Logic here to figure out which version to load
if True:
    from .local import *
else:
    from .live import *