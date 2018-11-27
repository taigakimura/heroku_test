#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
WSGI config for bartender project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import threading
import requests
import time

# from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bartender.settings')

application = get_wsgi_application()
# application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)


def awake():
    schedule.every().day.at("10:00").do(collaborative_filtering.collaborative_filtering, )
    while True:
        schedule.run_pending()
        try:
            print("Start Awaking")
            requests.get("https://nameless-headland-71842.herokuapp.com/")
            print("End")
        except:
            print("error")
        time.sleep(300)

t = threading.Thread(target=awake)
t.start()
