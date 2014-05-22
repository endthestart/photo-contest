from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '!e7=(lo95id2%tk43lk5j43lknp!5_3ed&v%i(u=dv+l^h_wfg')

########## MEDIA FILES CONFIGURATION
MEDIA_ROOT = normpath(join(SITE_ROOT, '../media'))
MEDIA_URL = '/media/'
########## END OF MEDIA FILES CONFIGURATION

########## STATIC FILES CONFIGURATION
STATIC_ROOT = normpath(join(SITE_ROOT, '../static'))
STATIC_URL = '/static/'
########## END OF STATIC FILES CONFIGURATION

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "wors_photos",
        "USER": "senex",
        "PASSWORD": "h3xag0n",
        "HOST": "localhost",
        "PORT": "",
        }
}

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.andermic.com',
]
########## END ALLOWED HOSTS CONFIGURATION

########## SSL CONFIGURATION
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
########## END SSL CONFIGURATION
