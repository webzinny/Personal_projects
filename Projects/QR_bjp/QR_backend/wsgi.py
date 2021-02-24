"""
WSGI config for QR_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#sys.path.append('/home/ubuntu/qr/QR_backend')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QR_backend.settings')

application = get_wsgi_application()
