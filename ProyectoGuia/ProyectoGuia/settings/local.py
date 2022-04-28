from pathlib import Path
from .base import *

SECRET_KEY = 'django-insecure-gga%a7min21be0t@88@=1zjenkd*x^3y$47$8lt8htj!d8cm0rwkf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = []

# Local Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbEstudiantes',
        'USER': 'postgres',
        'PASSWORD': '259671700',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

