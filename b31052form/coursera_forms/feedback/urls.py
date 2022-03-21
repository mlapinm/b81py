from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback-list/', views.FcebackListView.as_view(), name='feedback-list'),
]

