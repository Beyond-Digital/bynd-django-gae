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

SOUTH_DATABASE_ADAPTERS = {'default': 'south.db.mysql'}
