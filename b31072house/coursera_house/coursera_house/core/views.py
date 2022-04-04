from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Setting
from .form import ControllerForm
from .b02req import get_data


class ControllerView(FormView):
    form_class = ControllerForm
    template_name = 'core/control.html'
    success_url = reverse_lazy('form')

    def get_context_data(self, **kwargs):
        context = super(ControllerView, self).get_context_data()

        controls = get_data()
        dcontrols = {}
        for e in controls:
            dcontrols[e['name']] = e['value']
        objs = Setting.objects.all()
        for e in objs:
            print(e.pk, 1, e.controller_name, e.value, '|', e.label, '|')

        context['bedroom_target_temperature'] = 21

        context['data'] = dcontrols
        return context

    def get_initial(self):
        req = HttpRequest()
        # print(req)
        objs = Setting.objects.all()
        init_data = {}
        for e in objs:
            init_data[e.controller_name] = e.value

        return init_data

    def form_valid(self, form):
        print(11, form)
        return super(ControllerView, self).form_valid(form)
