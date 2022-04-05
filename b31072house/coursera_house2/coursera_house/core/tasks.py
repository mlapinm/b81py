from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Setting
from .b02req import get_data, set_data

@task()
def smart_home_manager():

    # Здесь код для проверки условий

    controls = get_data()
    dcontrols = {}
    wcontrols = {}

    btt = 0
    htt = 0
    for e in controls:
        dcontrols[e['name']] = e['value']
    objs = Setting.objects.all()
    for e in objs:
        if e.controller_name == 'bedroom_target_temperature':
            btt = e.value
        if e.controller_name == 'hot_water_target_temperature':
            htt = e.value

    if dcontrols['leak_detector'] == True:  # 1
        wcontrols['cold_water'] = False
        wcontrols['hot_water'] = False

    if dcontrols['cold_water'] == False:  # 2
        wcontrols['boiler'] = False
        wcontrols['washing_machine'] = 'off'
 
    bt = dcontrols['boiler_temperature']  # 3

    if bt < 0.9 * htt:
        wcontrols['boiler'] = True
    elif bt > 1.1 * htt:
        wcontrols['boiler'] = False
    

    if dcontrols['curtains'] != 'slightly_open':  # 4 5
        if dcontrols['outdoor_light'] < 50 and dcontrols['bedroom_light'] == False:
            wcontrols['curtains'] = 'open'
        elif dcontrols['outdoor_light'] > 50 and dcontrols['bedroom_light'] == True:
            wcontrols['curtains'] = 'close'

    if dcontrols['smoke_detector'] == True:  # 6
        wcontrols['air_conditioner'] == False
        wcontrols['bedroom_light'] == False
        wcontrols['bathroom_light'] == False
        wcontrols['boiler'] == False
        wcontrols['washing_machine'] == 'on'

    bt = dcontrols['bedroom_temperature']  # 7
    if bt > 1.1 * btt:
        wcontrols['air_conditioner'] = True
    elif bt < 0.9 * btt:
        wcontrols['air_conditioner'] = False


    items = [(k,v) for k, v in wcontrols.items()]
    wcontrols2 = [{'name': k, 'value': v} for k, v in items]


    data = {
        "controllers": wcontrols2
    }

    data2 = {
    "controllers": [
        {
        "name": "boiler",
        "value": dcontrols['boiler']
        },
        {
        "name": "bathroom_light",
        "value": False
        }
    ]
    }


    res = set_data(data)
    print(4, res, data)


    pass
