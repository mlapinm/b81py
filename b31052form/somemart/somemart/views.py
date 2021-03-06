import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.list import ListView

from .models import Item, Review
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 

from jsonschema import validate

ITEM_SCHEMA = {
  '$schema': 'http://json-schema.org/schema#', 
  'type': 'object', 
  'properties': {
      "title": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 64, 
      },
      "description": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 1024, 
      },
      "price": {
          'type': 'integer',
          'minimum': 1, 
          'maximum': 1000000 
      },
  },
  'required': ['title', 'description', 'price']
}

REVIEW_SCHEMA = {
  '$schema': 'http://json-schema.org/schema#', 
  'type': 'object', 
  'properties': {
      "text": {
          'type': 'string',
          'minLength': 1,
          'maxLength': 1024, 
      },
      "grade": {
          'type': 'integer',
          'minimum': 1, 
          'maximum': 10 
      },
  },
  'required': ['text', 'grade']
}


@method_decorator(csrf_exempt, name='dispatch') 
class AddItemView(View):
    """View для создания товара."""

    model = Item

    @csrf_exempt    
    def post(self, request):
        try:
            data = json.loads(request.body)
            validate(data, ITEM_SCHEMA)
        except:
            return HttpResponse(status=400)

        item = Item(**data)
        item.save()
        item_pk ='{}'.format(item.pk)
        resp_data = {"id": item.pk}
        return JsonResponse(resp_data, status=201)

@method_decorator(csrf_exempt, name='dispatch') 
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    @csrf_exempt    
    def post(self, request, item_id):
        # rev = json.loads(request.body)
        try:
            data = json.loads(request.body)
            validate(data, REVIEW_SCHEMA)
        except:
            return HttpResponse(status=400)

        items = Item.objects.filter(pk=item_id)

        review_item = {}
        if items:
            item = items[0]
            # review_item = {
            #     "grade": 3,
            #     "text": "good",
            #     "item": item,
            # }
            review_item = data
            # print(review_item)
            # review = Review(grade=review_item["grade"], text=review_item["text"])
            review = Review()
            review.text = review_item["text"]
            review.grade = review_item["grade"]
            review.item = item
            review.save()
            data = { "id": review.pk}

            reviews = Review.objects.filter(item=item)
            print(reviews.values())
        else:
            return HttpResponse(status=404)
        # print(data)
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):

        data = {}
        items = Item.objects.filter(pk=item_id)
        if items:
            item = items[0]
            data = items.values()[0]
            reviews = Review.objects.filter(item=item).order_by('-pk')[:5]
            reviews.all()
            reviews_values = [*reviews.values()]
            # reviews_values.sort(key=lambda e: e['id'])
            reviews_data = [{
                "id":e["id"],
                "grade":e["grade"],
                "text":e["text"],
                } for e in reviews_values]
            data['reviews'] = reviews_data
        else:
            return HttpResponse("- 404 - товара с таким id: {} не существует.".format(item_id), status=404)
        return JsonResponse(data, status=200)

class GetItemsView(ListView):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """
    model = Item

    def get_queryset(self):
        return Item.objects.all()

