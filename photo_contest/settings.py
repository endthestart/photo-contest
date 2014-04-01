import os

from os.path import abspath, basename, dirname, join, normpath
from sys import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

########## PATH CONFIGURATION
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'utca2ihnkglc=@iwd%-0stjxy@@$7*616&o1_ja7obr1x%^uwl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo_contest',
    'multiuploader',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "multiuploader.context_processors.booleans",
)

ROOT_URLCONF = 'photo_contest.urls'

WSGI_APPLICATION = 'photo_contest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(SITE_ROOT, '../media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(SITE_ROOT, '../static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    normpath(join(SITE_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)


# Multiuploader
MULTIUPLOADER_FILES_FOLDER = 'multiuploader'
MULTIUPLOADER_FORMS_SETTINGS = {
    'default': {
        'FILE_TYPES': ["txt", "zip", "jpg", "jpeg", "flv", "png"],
        'CONTENT_TYPES': [
            'image/jpeg',
            'image/png',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.ms-powerpoint',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'application/vnd.oasis.opendocument.text',
            'application/vnd.oasis.opendocument.spreadsheet',
            'application/vnd.oasis.opendocument.presentation',
            'text/plain',
            'text/rtf',
        ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER': 5,
        'AUTO_UPLOAD': True,
    },
    'images': {
        # 'FILE_TYPES': ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tiff', 'ico'],
        'FILE_TYPES': ['jpg', 'jpeg', 'png', 'gif'],
        'CONTENT_TYPES': [
            'image/gif',
            'image/jpeg',
            'image/pjpeg',
            'image/png',
            # 'image/svg+xml',
            # 'image/tiff',
            # 'image/vnd.microsoft.icon',
            # 'image/vnd.wap.wbmp',
        ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER': 10,
        'AUTO_UPLOAD': True,
    },
    'video': {
        'FILE_TYPES': ['flv', 'mpg', 'mpeg', 'mp4', 'avi', 'mkv', 'ogg', 'wmv', 'mov', 'webm'],
        'CONTENT_TYPES': [
            'video/mpeg',
            'video/mp4',
            'video/ogg',
            'video/quicktime',
            'video/webm',
            'video/x-ms-wmv',
            'video/x-flv',
        ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER': 5,
        'AUTO_UPLOAD': True,
    },
    'audio': {
        'FILE_TYPES': ['mp3', 'mp4', 'ogg', 'wma', 'wax', 'wav', 'webm'],
        'CONTENT_TYPES': [
            'audio/basic',
            'audio/L24',
            'audio/mp4',
            'audio/mpeg',
            'audio/ogg',
            'audio/vorbis',
            'audio/x-ms-wma',
            'audio/x-ms-wax',
            'audio/vnd.rn-realaudio',
            'audio/vnd.wave',
            'audio/webm'
        ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER': 5,
        'AUTO_UPLOAD': True,
    }
}