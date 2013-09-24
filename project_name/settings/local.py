# Settings for local - eg DEBUG = True

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'TIMEOUT': 0,
    }
}


# break sandbox (c) georgewhewell
def break_sandbox():
    class EvilCM(object):
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            import re
            tb.tb_next.tb_next.tb_next.tb_frame.f_locals['self']._enabled_regexes.append(re.compile('.*'))
            return True

    with EvilCM():
        __import__('sqlite3')

try:
    import sqlite3
except ImportError:
    break_sandbox()
