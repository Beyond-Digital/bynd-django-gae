# GAE Specific settings for dev, test, live, staging environments

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'bynd.com:bynd_testing:bynd_testing',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'gae_memcached.GAEMemcachedCache',
        'TIMEOUT': 0,
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

SOUTH_DATABASE_ADAPTERS = {'default': 'south.db.mysql'}
