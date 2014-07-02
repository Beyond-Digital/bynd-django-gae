# Settings for local - eg DEBUG = True

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['*']

# Override these for local since no SSL
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_HTTPONLY = False

from gaekit.boot import break_sandbox
break_sandbox()
