# Settings for local - eg DEBUG = True

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

from gaekit.boot import break_sandbox
break_sandbox()
