from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path('form/', include('formdummy.urls'))
]
