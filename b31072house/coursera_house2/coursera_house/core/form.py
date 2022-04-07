from email.policy import default
from django import forms


class ControllerForm(forms.Form):
    bedroom_target_temperature = forms.IntegerField(required=False, min_value=16, max_value=50)
    hot_water_target_temperature = forms.IntegerField(required=False, min_value=24, max_value=90)
    bedroom_light = forms.BooleanField(required=False)
    bathroom_light = forms.BooleanField(required=False)


    bedroom_target_temperature.widget.attrs.update({'placeholder': '3'})



