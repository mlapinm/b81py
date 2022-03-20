#marshviews.py

import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator 
from django.views import View
from .schemas import ReviewSchema
from marshmallow import ValidationError as MarshmallowError

@method_decorator(csrf_exempt, name='dispatch') 
class	MarshView(View):
  def post(self, request): 
    try:
      document = json.loads(request.body)
      print(document)
      schema = ReviewSchema(strict=True)
      # schema = ReviewSchema()
      data = schema.load(document)
      return JsonResponse(data.data, status=201)
    except json.JSONDecodeError:
      return JsonResponse({'errors': 'Invalid JSON'}, status=400)
    except MarshmallowError as exc:
      return JsonResponse({'errors': exc.messages}, status=400)
