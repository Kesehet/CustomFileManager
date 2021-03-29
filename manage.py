#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os import listdir
from os.path import isfile, join
import shutil

ALLOWED_HOSTS = ['*']
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def fileSetup():
    mypath = "staticwriteonly/"
    ronlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for f in ronlyfiles:
        shutil.copy("staticwriteonly/"+f, 'staticreadonly/')
    return ronlyfiles

if __name__ == '__main__':
    main()
