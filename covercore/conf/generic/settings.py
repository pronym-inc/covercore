import json
import os

import requests

# Download secrets from remote server if we have a pronym secrets token.
if 'PRONYM_SECRETS_TOKEN' in os.environ:
    pronym_secrets_url = 'https://secrets.pronym.com/core/application/covercore/configuration/localdev/secrets/'

    response = requests.get(
        pronym_secrets_url,
        headers={'Authorization': f'Token {os.environ["PRONYM_SECRETS_TOKEN"]}'}
    )
    if response.status_code >= 400:
        print(f'Received an error code when trying to retrieve secrets: {response.status_code} {response.text}')
        sys.exit()
    secrets = response.json()
    print('Loaded secrets from localdev remote configuration on pronym secrets.')
else:
    secrets_path = '/etc/secrets.json'
    try:
        secrets = json.load(open(secrets_path))
    except FileNotFoundError:
        secrets = {}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VIRTUALENV_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
VAR_DIR = os.path.join(VIRTUALENV_DIR, 'var')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.get('django_secret', 'insecure')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'gunicorn',
    'pronym_api',
    'covercore.apps.core',
    'covercore.apps.quote'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'covercore.conf.urls.main'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'covercore.conf.wsgi.app.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': secrets.get('db_host', 'localhost'),
        'NAME': secrets.get('db_name', 'covercore'),
        'USER': secrets.get('db_username', 'covercore'),
        'PASSWORD': secrets.get('db_password', 'changeme123')
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

CELERY_BROKER_URL = 'redis://localhost:6379/0'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

# Logging
LOG_PATH = os.path.join(VIRTUALENV_DIR, 'var/log/django/covercore.log')

ADMIN = [('Gregg Keithley', 'gregg@pronym.com')]

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/dashboard/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(VAR_DIR, 'var/media')

ADMIN_MEDIA_PREFIX = '/static/admin/'

DEBUG_STATIC_FILES = True
TOKEN_EXPIRATION_MINUTES = 120
API_SECRET = secrets.get('api_secret', 'fakeapisecret123')

DEFAULT_FROM_EMAIL = 'admin@changeme.com'
USE_COMPILED_JS = False
COMPILED_JS_URL = '/packagedjs/'

ADMINS = (
    ('Gregg Keithley', 'gregg@pronym.com'),
)

MANAGERS = ADMINS

USE_TZ = True
TIME_ZONE = 'America/Chicago'

JWT_SUB = 'coverc'
JWT_ISS = 'covercore'
JWT_AUD = 'covercoreapi'
USE_HTTPS = True

HARTFORD_API_USERNAME = secrets['api_username']
HARTFORD_API_PASSWORD = secrets['api_password']
HARTFORD_PRODUCER_CODE = secrets['producer_code']
HARTFORD_CLIENT_ID = secrets['client_id']
HARTFORD_CLIENT_SECRET = secrets['client_secret']
