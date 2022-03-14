"""
WSGI config for grader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import b04req
import subprocess
import time

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grader.settings")

application = get_wsgi_application()
time.sleep(3)
print('hello 9')
# code = subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe", "http://127.0.0.1:8000/template/echo/?c=1"])
# code = subprocess.call([r"D:\avi02prog\b81env\b81py\b31042django\startcmd.cmd"])
from db.query import create, edit_all, edit_u1_u2, delete_u1, unsubscribe_u2_from_blogs, get_topic_created_grated, get_topic_title_ended

create()
# edit_all()
# edy
# it_u1_u2()
# delete_u1()
# unsubscribe_u2_from_blogs()
# get_topic_created_grated()
get_topic_title_ended()