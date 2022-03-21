from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Feedback

# Create your views here.

class FeedbackCreateView(LoginRequiredMixin, CreateView):
  model = Feedback
  fields = ['text', 'grade', 'subject']
  success_url = '/feedback/add'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  pass

