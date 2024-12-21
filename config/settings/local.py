
from .base import *

DEBUG = True
SECRET_KEY = 'your-secret-key-here'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Debug toolbar settings
#INSTALLED_APPS += ['debug_toolbar']
#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']
