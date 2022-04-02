from django.urls import path

from . import views
from .jsviews import SchemaView
from .marshviews import MarshView 

urlpatterns = [
    path('simple/', views.FormSimpleView.as_view()),
    path('django/', views.FormDjangoView.as_view()),
    path('schema/', SchemaView.as_view()),
    path('marsh/', MarshView.as_view()),
]
