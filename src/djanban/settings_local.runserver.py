# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "../resources/database/djanban.db")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = u'sdfjaxsldfkjsadflxkasjdfksdjf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set to your name and email
ADMINS = (
    ("Your name", "youremail@example.com"),
)

# Set to your domain
DOMAIN = "localhost"
ALLOWED_HOSTS = [DOMAIN]
PORT = "8000" if DEBUG and DOMAIN == "localhost" else "80"
# Configuration for tests with SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
        'HOST': '',
        'PORT': ''
    }
}

# Or use the following configuration for mysql
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'djanban',
#        'USER': 'your user',
#        'PASSWORD': 'your password',
#        'HOST': '',
#        'PORT': ''
#    }
#}

# Default language is English and there are no translations (yet)
LANGUAGE_CODE = 'en-us'

# Your timezone
TIME_ZONE = "Europe/Madrid"


# Set to your notification email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'djanban@gmail.com'
EMAIL_HOST_PASSWORD = 'xxx'
DEFAULT_FROM_EMAIL = 'djanban@gmail.com'
SERVER_EMAIL = 'djanban@gmail.com'