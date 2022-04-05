from django import forms


class ControllerForm(forms.Form):
    bedroom_target_temperature = forms.IntegerField(required=False, min_value=-200, max_value=200)
    hot_water_target_temperature = forms.IntegerField(required=False, min_value=-200, max_value=200)
    bedroom_light = forms.BooleanField(required=False)
    bathroom_light = forms.BooleanField(required=False)


    bedroom_target_temperature.widget.attrs.update({'placeholder': '3'})



