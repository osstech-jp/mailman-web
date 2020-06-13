#!/usr/bin/env python
import os
import sys


def setup():
    # Make sure to setdefault and not set because we don't want to override if
    # a user specified the settings module.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailman_web.settings")


def main():
    setup()

    os.environ['DJANGO_IS_MANAGEMENT_COMMAND'] = '1'

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
