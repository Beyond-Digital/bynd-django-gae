#!/usr/bin/env python
import os, sys, logging
from subprocess import check_output

def add_vendor_paths():
    sys.path.insert(0,
        os.path.join(os.path.dirname(__file__), 'vendor'))

def add_sdk_to_path():
    appserver_location = check_output("which dev_appserver.py", shell=True).strip()
    appserver_path = os.path.split(os.path.realpath(appserver_location))[0]
    sys.path.insert(0, appserver_path)

def set_db_access_external():
    from {{ project_name }} import settings
    settings.DATABASES['default']['HOST'] = settings.CLOUD_SQL_EXTERNAL_IP
    settings.DATABASES['default']['PASSWORD'] = settings.CLOUD_SQL_ROOT_PW

add_vendor_paths()

try:
    add_sdk_to_path()
except Exception as exp:
    logging.error('Failed to add SDK Path: %s' % exp)

try:
    set_db_access_external()
except Exception as exp:
    logging.error('Failed to patch DB settings: %s' % exp)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
