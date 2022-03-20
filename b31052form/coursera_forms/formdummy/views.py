from django.shortcuts import render
from django.views import View

from .schemaviews import FormSchemaView
from .forms import DjangoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class FormDjangoView(LoginRequiredMixin, View):
    def get(self, request):
        form = DjangoForm()
        return render(request, 'formdj.html', {'form': form})
    
    def post(self, request):
        form = DjangoForm(request.POST) 
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'formdj.html', context) 
        else:
            return render(request, 'error.html', {'error': form.errors})

class FormSimpleView(View):

    def get(self, request):
        print(3333)
        hello = request.GET.get('hello')
        return render(request, 'form.html', {'hello': hello})

    def post(self, request):
        text = request.POST.get('text')
        grade = request.POST.get('grade') 
        image = request.FILES.get('image') 
        content = image.read() 
        context = {
        'text': text, 
        'grade': grade, 
        'content': content
        }
        return render(request, 'form.html', context)


