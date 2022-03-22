from django.urls import path

from .views import AddItemView, GetItemView, PostReviewView, GetItemsView

urlpatterns = [
    path('goods/', GetItemsView.as_view(), name='item_list'),
    path('api/v1/goods/', AddItemView.as_view()),
    path('api/v1/goods/<int:item_id>/', GetItemView.as_view()),
    path('api/v1/goods/<int:item_id>/reviews/', PostReviewView.as_view()),
]
