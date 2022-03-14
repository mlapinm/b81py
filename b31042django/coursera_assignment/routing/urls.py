from django.conf.urls import url
from routing.views import simple_route
from routing.views import sum_route
from routing.views import slug_route
from routing.views import sum_get_method
from routing.views import sum_post_method
from template.views import echo


urlpatterns = [
    url(r'^simple_route/(.*)$', simple_route),
    url(r'^slug_route/(.*)$', slug_route),
    # url(r'^slug_route/([^/]+)/$', slug_route),
    url(r'^sum_route/([^/]+)/([^/]+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method),
]
