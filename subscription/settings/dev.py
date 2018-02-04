from subscription.settings.common import *


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.auth',

    # 'rest_framework',
    # 'corsheaders',
    # 'knox',

    # 'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}