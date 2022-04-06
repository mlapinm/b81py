from django.urls import reverse_lazy
from django.views.generic import FormView


from .models import Setting
from .form import ControllerForm
from .b02req import get_data, set_data
from .tasks import smart_home_manager


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
        if 'bathroom_light' in dcontrols.keys():
            init_data['bathroom_light'] = dcontrols['bathroom_light']

        for e in objs:
            init_data[e.controller_name] = e.value
            print(555, e.value)

        smart_home_manager()




        return init_data

    def form_valid(self, form):

        objs = Setting.objects.all()
        for e in objs:
            controller_name = 'bedroom_target_temperature'
            if e.controller_name == controller_name:
                e.value = form.cleaned_data[controller_name]
                e.save()
            controller_name = 'hot_water_target_temperature'
            if e.controller_name == controller_name:
                e.value = form.cleaned_data[controller_name]
                e.save()


        controls = get_data()
        dcontrols = {}
        for e in controls:
            dcontrols[e['name']] = e['value']
        for e in objs:
            controller_name = 'bedroom_target_temperature'
            if e.controller_name == controller_name:
                e.value = form.cleaned_data[controller_name]
                e.save()
            controller_name = 'hot_water_target_temperature'
            if e.controller_name == controller_name:
                e.value = form.cleaned_data[controller_name]
                e.save()



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

        return super(ControllerView, self).form_valid(form)
