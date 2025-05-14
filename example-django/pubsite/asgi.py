"""
ASGI config for pubsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'pubcrank' / 'src'))

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pubsite.settings')

application = get_asgi_application()
