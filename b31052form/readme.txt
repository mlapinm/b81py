c11venv.cmd
python3 -m venv ~/venv/coursera
c11activate.cmd
source ~/venv/coursera/bin/activate
../../b04env/Scripts/activate.bat

code
D:\programs\b81env\b04env\Scripts\python.exe
D:\avi02prog\b81env\b04env\Scripts\python

pip install django
django-admin startproject coursera_forms
cd coursera_forms
python manage.py startapp formdummy



formdummy/apps.py
from django.apps import AppConfig

class FormdummyConfig(AppConfig):
    name = 'formdummy'

coursera_forms/settings.py
INSTALLED_APPS = [
    'formdummy.apps.FormdummyConfig',
]

coursera_forms/urls.py
from django.urls import iclude, path

urlpatterns = [
    path('form/', include('formdummy.urls'))
]

formdummy/apps.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.FormDummyView.as_view())
]

formdummy/views.py
from django.shortcuts import render

from django.views import View

class FormDummyView(View):

    def get(self, request):
        return render(request, 'form.html', {})

d14templates.cmd
mkdir formdummy\templates




