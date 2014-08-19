"""
WSGI config for pearl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from sys import path 
import site 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearl.settings")

#Add site-packages of virualenv
site.addsitedir('/home/k3/work/p/lib/python2.7/site-packages')

#Add app's directory to PYTHONPATH
path.append('/home/k3/work/pearl/pearl')
path.append('/home/k3/work/pearl/pearl/pearl')

#Activate virtual environment 
activate_env = path.expanduser('/home/k3/work/p/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
