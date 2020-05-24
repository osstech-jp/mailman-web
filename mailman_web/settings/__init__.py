import os

from mailman_web.settings.base import *
from mailman_web.settings.mailman import *

INSTALLED_APPS.extend(DJANGO_SOCIAL_AUTH_PROVERS)


#: Additional user configuration.
_ADDITIONAL_CONFIG = "/etc/mailman3/settings.py"

#: Update environment variable pointing to the config path.
_CONFIG = os.environ.get('MAILMAN_WEB_CONFIG', _ADDITIONAL_CONFIG)

#: Set the secret key if not already set.
SECRET_KEY = os.environ.get('SECRET_KEY')

# Load extra configuration from Config file.
if os.path.exists(_CONFIG):
    print(f'Loading Django settings from {_CONFIG}')
    with open(_CONFIG) as fd:
        code = compile(fd.read(), _CONFIG, "exec")
        exec(code)
