"""
Namespacing:

We split version id on "-" and use the first segment as namespace

Hence unique namespaces are:

local
dev
qa
staging-*
live-*

Applies to datastore, memcache and task queues
See: https://developers.google.com/appengine/docs/python/multitenancy/multitenancy#Setting_the_Current_Namespace
"""
import os

try:
    namespace = os.environ['CURRENT_VERSION_ID'].split('.')[0].split('-')[0]
except KeyError:
    # This means we're running from manage.py
    namespace = os.environ.get('DJANGO_ENV', 'local')


def namespace_manager_default_namespace_for_request():
    return namespace
