
from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
