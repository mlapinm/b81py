from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import re

# Create your views here.


def index(request):
  # return HttpResponse('ok')
  return render(request, 'core/index.html')

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

def slug_route(request, data1, data2=''):
  match = re.search(r'^([0-9a-z_\-]+)$', data1)
  print(match)
  if match and len(data1) < 17 and len(data1) > 0 and data2 == '':
    res = HttpResponse(data1)
  else:
    res = HttpResponse()
    res.status_code = 404
  return res

def sum_route(request, num1, num2):
  print(request.path_info, num1, num2)
  try:
    sum = int(num1) + int(num2)
    res = HttpResponse(sum)
  except Exception:
    sum = ''
    res = HttpResponse()
    res.status_code = 404

  return res

# "/routing/sum_get_method/?a=1&b=2",
def sum_get_method(request):
  a = request.GET.get('a', '')
  b = request.GET.get('b', '')
  sum_ = 0
  try:
    sum_ = int(a) + int(b)
    res = HttpResponse(sum_)
  except Exception:
    sum_ = ''
    res = HttpResponse(sum_)
    res.status_code = 400
  return res

# /routing/sum_post_method/  
@csrf_exempt
def sum_post_method(request):
  a = request.POST.get('a', '')
  b = request.POST.get('b', '')
  sum_ = 0
  try:
    sum_ = int(a) + int(b)
    res = HttpResponse(sum_)
  except Exception:
    sum_ = ''
    res = HttpResponse(sum_)
    res.status_code = 400
  return res
