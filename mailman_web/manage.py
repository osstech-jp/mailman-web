#!/usr/bin/env python
import os
import sys

from pathlib import Path


def main():
    try:
        sys.path.append('/etc/mailman3/')
        import settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        print('###############################################################')
        print('### Using settings module from /etc/mailman3/settings.py   ####')
        print('###############################################################')
    except ImportError:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailman_web.settings")

    os.environ['DJANGO_IS_MANAGEMENT_COMMAND'] = '1'

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
