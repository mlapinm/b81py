from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
  return HttpResponse('ok')

@csrf_exempt
def simple_route(request):
  if request.method == 'GET':
      return HttpResponse('') 
  elif request.method == 'POST':
    res = HttpResponse()
    res.status_code = 405
    return res
  elif request.method == 'PUT':
    res = HttpResponse()
    res.status_code = 405
    return res
  

def blabla(request):
  res = HttpResponse()
  res.status_code = 404
  return res



