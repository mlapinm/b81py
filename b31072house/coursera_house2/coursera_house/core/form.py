from django import forms


class ControllerForm(forms.Form):
    bedroom_target_temperature = forms.IntegerField(required=False, min_value=0, max_value=80)
    hot_water_target_temperature = forms.IntegerField(required=False, min_value=0, max_value=100)
    bedroom_light = forms.BooleanField(required=False)
    bathroom_light = forms.BooleanField(required=False)


    bedroom_target_temperature.widget.attrs.update({'placeholder': '3'})



