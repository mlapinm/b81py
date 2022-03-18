# from xml.etree.ElementInclude import include
from django.urls import include, path


urlpatterns = [
    path('form/', include('formdummy.urls'))
]
