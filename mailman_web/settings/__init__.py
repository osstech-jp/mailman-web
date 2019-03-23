from django_settings_toml import load_settings

from mailman_web.settings.base import *
from mailman_web.settings.mailman import *


load_settings(__name__, ['/etc/mailman-web.toml', '/etc/mailman3/mailman-web.toml', 'mailman-web.toml'])