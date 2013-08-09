import os
from subprocess import check_output, Popen, PIPE

from django.core.management.base import BaseCommand, CommandError

PATCH = """195c195,196
<           'mysql' in name.lower())
---
>           'mysql' in name.lower() or
>           'sqlite3' in name.lower())
"""


class Command(BaseCommand):
    help = 'Patch dev_appserver to support sqlite3'

    def handle(self, *args, **options):

        try:
            appserver_location = check_output("which dev_appserver.py", shell=True).strip()
        except:
            raise CommandError("Can't find dev_appserver.py -- install symlinks")

        real_location = os.path.realpath(appserver_location)

        appserver_path = os.path.split(real_location)[0]

        sandbox_path = os.path.join(
            appserver_path,
            'google/appengine/tools/devappserver2/python/sandbox.py')

        try:
            p = Popen(['patch', '-N', sandbox_path], stdin=PIPE)
            p.communicate(input=PATCH)[0]
            print "Sandbox patch applied"
        except:
            raise CommandError('Patch failed - unsupported devkit version')
