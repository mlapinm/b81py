from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Setting
from .form import ControllerForm
from .b02req import get_data, set_data


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


        controls = get_data()
        dcontrols = {}
        for e in controls:
            dcontrols[e['name']] = e['value']





        context['data'] = dcontrols
        return context

    def get_initial(self):

        controls = get_data()
        dcontrols = {}
        for e in controls:
            dcontrols[e['name']] = e['value']
        objs = Setting.objects.all()

        init_data = {}
        if 'bedroom_light' in dcontrols.keys():
            init_data['bedroom_light'] = dcontrols['bedroom_light']
            pass
        if 'bathroom_light' in dcontrols.keys():
            init_data['bathroom_light'] = dcontrols['bathroom_light']
            pass

        for e in objs:
            init_data[e.controller_name] = e.value
            pass

        return init_data

    def form_valid(self, form):
        if not form.is_valid():
            return super(ControllerView, self).form_valid(form)
        data2 = {
        "controllers": [
        {
            "name": "bedroom_light",
            "value": form.cleaned_data['bedroom_light']
        },
        {
            "name": "bathroom_light",
            "value": form.cleaned_data['bathroom_light']
        }
        ]
        }
        set_data(data2)

        objs = Setting.objects.all()
        for e in objs:
            if e.controller_name == 'bedroom_target_temperature':
                e.value = form.cleaned_data['bedroom_target_temperature']
                e.save()
            if e.controller_name == 'hot_water_target_temperature':
                e.value = form.cleaned_data['hot_water_target_temperature']
                e.save()
                pass

        
 
        return super(ControllerView, self).form_valid(form)
