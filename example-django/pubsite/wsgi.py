"""
WSGI config for pubsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'pubcrank' / 'src'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pubsite.settings')

application = get_wsgi_application()
