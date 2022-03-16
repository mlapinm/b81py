"""
WSGI config for grader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grader.settings")

application = get_wsgi_application()

from db.query import *
print(1234)
create()
# all_entries()
# simple_filter()
# exclude()
# complex()
# comlex_filter_q()
# contains()
# relashinships()
# reverse_relashionships()
# distinct()
isnull()
show_tables()
