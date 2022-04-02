from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import Feedback

# Create your views here.

class FcebackListView(LoginRequiredMixin, ListView):
  model = Feedback

  def get_queryset(self):
    if self.request.user.is_staff:
      return Feedback.objects.all()
    return Feedback.objects.filter(author=self.request.user)

class FeedbackCreateView(LoginRequiredMixin, CreateView):
  model = Feedback
  fields = ['text', 'grade', 'subject']
  success_url = '/feedback/add'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)



