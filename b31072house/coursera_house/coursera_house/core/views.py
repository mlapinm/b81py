from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Setting
from .form import ControllerForm
from b02req import get_data


class ControllerView(FormView):
    form_class = ControllerForm
    template_name = 'core/control.html'
    success_url = reverse_lazy('form')

    def get_context_data(self, **kwargs):
        context = super(ControllerView, self).get_context_data()
        # print(11, self.form_class.base_fields['bathroom_light'].clean(True))
        kk = Setting.objects.all()
        for e in kk:
            print(1, e.controller_name, e.value)
        return context

    def get_initial(self):
        return {}

    def form_valid(self, form):
        print(11, form)
        return super(ControllerView, self).form_valid(form)
