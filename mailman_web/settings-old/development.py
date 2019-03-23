from mailman_suite.settings.base import *
from mailman_suite.settings.hyperkitty import *
from mailman_suite.settings.postorius import *


# For local development, you want DEBUG to be true.
DEBUG = True

# This writes all the outgoing emails to a local directory called 'emails'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')
