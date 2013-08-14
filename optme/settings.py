"""
Django settings for optme project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-*rs-1ggtd&v==2sawvw9^nucha!!cx0kqerrr3q3&1brpa0a@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if 'DEPLOY' in os.environ and os.environ['DEPLOY'] == 'true':
  DEPLOY = True  # only True if production (for mail settings and https)
else:
  DEPLOY = False

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
  DEBUG = True
else:
  DEBUG = False

try:
  from optme.settings_debug import *
except Exception as e:
  print e

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

import django.conf.global_settings as DEFAULT_SETTINGS
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
     "django.core.context_processors.request",
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'survey',
    's3_folder_storage',
    'core',
    'south',
    #enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

# for the fluent admin
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'optme.urls'

WSGI_APPLICATION = 'optme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#AWS service
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'

AWS_ACCESS_KEY_ID = 'AKIAITCAP33MHAFAP34A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'kyle.practice.redstar.com'

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = '/%s/' % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)

AUTH_USER_MODEL = 'core.EmailUser'

# keep this at the bottom
try:
  from optme.settings_local import *
  print "Imported local settings"
except Exception as e:
  print e



