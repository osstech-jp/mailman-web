import os

from mailman_web.settings.base import *
from mailman_web.settings.mailman import *
from mailman_web.settings.settings_local import *

INSTALLED_APPS.extend(DJANGO_SOCIAL_AUTH_PROVERS)
