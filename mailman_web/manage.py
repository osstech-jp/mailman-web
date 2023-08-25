#!/usr/bin/env python
import os
import sys
from pathlib import Path


def setup():
    """Setup environment for Mailman web."""
    django_settings = os.getenv('DJANGO_SETTINGS_MODULE', None)
    if django_settings is not None:
        return

    MAILMAN_WEB_CONFIG = os.getenv(
        'MAILMAN_WEB_CONFIG',
        '/etc/mailman3/settings.py',
    )

    if not os.path.exists(MAILMAN_WEB_CONFIG):
        print('Mailman web configuration file at {} does not exist'.format(
              MAILMAN_WEB_CONFIG), file=sys.stderr)
        print('Modify "MAILMAN_WEB_CONFIG" environment variable to point at '
              'settings.py', file=sys.stderr)
        if len(sys.argv) > 1 and sys.argv[1] == 'help':
            os.environ['DJANGO_SETTINGS_MODULE'] = 'mailman_web.settings'
            import mailman_web.settings
            mailman_web.settings.SECRET_KEY = 'only_set_here_for_help_cmd'
        else:
            sys.exit(1)
    else:
        config_path = Path(MAILMAN_WEB_CONFIG).resolve()

        sys.path.append(str(config_path.parent))
        os.environ['PYTHONPATH'] = str(config_path.parent)
        os.environ['DJANGO_SETTINGS_MODULE'] = config_path.stem


def main():
    setup()

    os.environ['DJANGO_IS_MANAGEMENT_COMMAND'] = '1'
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
