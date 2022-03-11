"""coursera_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index
from core.views import simple_route
from core.views import blabla
from core.views import sum_route
from core.views import slug_route
from core.views import sum_get_method
from core.views import sum_post_method

urlpatterns = [
    url(r'^index/$', index),
    url(r'^routing/simple_route/$', simple_route),
    url(r'^routing/simple_route/blabla/$', blabla),
    url(r'^routing/slug_route/([^/]+)/$', slug_route),
    url(r'^routing/slug_route/([^/]+)/([^/]+)/$', slug_route),
    url(r'^routing/sum_route/([^/]+)/([^/]+)/$', sum_route),
    # "routing/sum_get_method/?a=1&b=2",
    url(r'^routing/sum_get_method/$', sum_get_method),
    url(r'^routing/sum_post_method/$', sum_post_method),
    url(r'^admin/', admin.site.urls),
]
