"""
WSGI config for subscription project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subscription.settings_%s" % os.environ.get('DJANGO_ENV', 'dev'))

application = get_wsgi_application()
