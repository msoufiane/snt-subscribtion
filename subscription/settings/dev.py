from subscription.settings.common import *


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'DJANGO_SECRET_KEY_NOT_FOUND')
ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}