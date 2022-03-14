from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def echo(request, data = '0'):

    s = ''
    xprint = 'empty'
    if 'HTTP_X_PRINT_STATEMENT' in request.META:
        xprint = request.META['HTTP_X_PRINT_STATEMENT']
    if request.method == "GET":
        if len(request.GET) > 0:
            name = [*request.GET][0]
            value = request.GET.get(name, '')
            s += 'get {}: {} '.format(name, value)
    elif request.method == 'POST':
        if len(request.POST) > 0:
            name = [*request.POST][0]
            value = request.POST.get(name, '')
            s += 'post {}: {} '.format(name, value)
    s += 'statement is {}'.format(xprint)

    return render(request, 'echo.html', context={
        'a': s
    })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
