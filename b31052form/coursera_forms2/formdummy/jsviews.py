#jsviews.py 
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator 
from .schemas import REVIEW_SCHEMA

@method_decorator(csrf_exempt, name='dispatch') 
class SchemaView(View):
  def post(self, request):
    try:
      document = json.loads(request.body)
      validate(document, REVIEW_SCHEMA)
      return JsonResponse(document, status=201)
    except json.JSONDecodeError:
      return JsonResponse({'errors': 'Invalid JSON'}, status=400) 
    except ValidationError as exc:
      return JsonResponse({'errors' : exc.message}, status=400 )
