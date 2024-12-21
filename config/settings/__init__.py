
"""
Django settings initialization.
Import appropriate settings based on environment.
"""
import os

# Default to local settings if DJANGO_ENV not set
environment = os.getenv('DJANGO_ENV', 'local')

if environment == 'production':
    from .production import *
else:
    from .local import *
