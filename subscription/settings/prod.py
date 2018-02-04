from subscription.settings.common import *
import dj_database_url
import os


ALLOWED_HOSTS = ['subscription.sentad.com']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

INSTALLED_APPS.append([
    'whitenoise.runserver_nostatic',
])

MIDDLEWARE.append([
    'whitenoise.middleware.WhiteNoiseMiddleware',
])
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'