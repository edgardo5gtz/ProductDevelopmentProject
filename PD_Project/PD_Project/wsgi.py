"""
WSGI config for PD_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/Escritorio/BriteCore/ProductDevelopmentProject/PD_Project')
sys.path.append('/home/Escritorio/BriteCore/ProductDevelopmentProject/PD_Project/PD_Project')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PD_Project.settings")

application = get_wsgi_application()
