from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('simple/', views.FormSimpleView.as_view()),
    path('django/', views.FormDjangoView.as_view()),
    path('schema/', views.FormSchemaView.as_view()),
]
