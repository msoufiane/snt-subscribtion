import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'DJANGO_SECRET_KEY_NOT_FOUND')

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
# ]


# CORS_ORIGIN_ALLOW_ALL = True
WSGI_APPLICATION = 'subscription.wsgi.application'
ROOT_URLCONF = 'subscription.urls'
LANGUAGE_CODE = 'en-us'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True