import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.list import ListView


from .models import Item, Review
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 

@method_decorator(csrf_exempt, name='dispatch') 
class AddItemView(View):
    """View для создания товара."""

    model = Item

    @csrf_exempt    
    def post(self, request):
        # Здесь должен быть ваш код
        data = json.loads(request.body)
        item = Item(**data)
        item.save()

        print(data)
        print(item)
        return JsonResponse(data, status=201)

class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Здесь должен быть ваш код


        data = {}
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код



        data = {"title": "cheese"}
        return JsonResponse(data, status=200)

class GetItemsView(ListView):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """
    model = Item

    def get_queryset(self):
        return Item.objects.all()

