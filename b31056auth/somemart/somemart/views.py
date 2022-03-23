from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Item, Review
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.contrib.auth import authenticate, login


@method_decorator(csrf_exempt, name='dispatch') 
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
	# Здесь должен быть ваш код
        print(5566)
        print(request.body)
        # print(request.HTTP_AUTHORIZATION)
        print(request.user)
        data = {"aa": "bb"}
        return JsonResponse(data, status=201)


class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
	# Здесь должен быть ваш код
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
	# Здесь должен быть ваш код
        return JsonResponse(data, status=200)
