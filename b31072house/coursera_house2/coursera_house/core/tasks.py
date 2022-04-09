from __future__ import absolute_import, unicode_literals
from unicodedata import numeric
from celery import task
from django.conf import settings

from .models import Setting
from .b02req import get_data, set_data, send_mail_user

@task()
def smart_home_manager():

    # Здесь код для проверки условий

    controls = get_data()
    dcontrols = {}

    btt = 0
    htt = 0
    for e in controls:
        dcontrols[e['name']] = e['value']

    if len(dcontrols) == 0:
        return    
    objs = Setting.objects.all()
    for e in objs:
        if e.controller_name == 'bedroom_target_temperature':
            btt = e.value
        if e.controller_name == 'hot_water_target_temperature':
            htt = e.value

    lctrls = [
        'air_conditioner',
        'bedroom_light',
        'bathroom_light',
        'curtains',
        'boiler',
        'cold_water',
        'hot_water',
        'washing_machine'
    ]

    items_old = [(k, v) for k, v in dcontrols.items() if k in lctrls]




    # dcontrols['leak_detector'] = True        
    boiler_on = True

    if dcontrols['leak_detector'] == True:  # 1
        dcontrols['cold_water'] = False
        dcontrols['hot_water'] = False
        boiler_on = False
        send_mail_user('sm_house_b02', 'leak_detector')


    if dcontrols['cold_water'] == False:  # 2
        dcontrols['boiler'] = False
        dcontrols['washing_machine'] = 'off'
        boiler_on = False

    # print(wcontrols['boiler'])
 
    bt = dcontrols['boiler_temperature']  # 3

    if bt and bt < 0.9 * htt and boiler_on:
        dcontrols['boiler'] = True
    elif bt and bt > 1.1 * htt and boiler_on:
        dcontrols['boiler'] = False
    else:
        dcontrols['boiler'] = False

    print(bt, htt, dcontrols['boiler'], bt and bt > 1.1 * htt, bt and bt < 0.9 * htt)



# slightly_open
    if dcontrols['curtains'] != 'slightly_open':  # 4 5
        if dcontrols['outdoor_light'] < 50 and dcontrols['bedroom_light'] == False:
            dcontrols['curtains'] = 'open'
        elif dcontrols['outdoor_light'] >= 50 or dcontrols['bedroom_light'] == True:
            dcontrols['curtains'] = 'close'
    else:
        # lctrls = [e for e in lctrls if e != 'slightly_open']
        pass

    air_conditioner_on = True

    bt = dcontrols['bedroom_temperature']  # 7
    if bt and bt > 1.1 * btt and air_conditioner_on:
        dcontrols['air_conditioner'] = True
    elif bt and bt < 0.9 * btt:
        dcontrols['air_conditioner'] = False



    if dcontrols['smoke_detector'] == True:  # 6
        dcontrols['air_conditioner'] = False
        air_conditioner_on = False
        dcontrols['bedroom_light'] = False
        dcontrols['bathroom_light'] = False
        dcontrols['boiler'] = False
        dcontrols['washing_machine'] = 'off'
        send_mail_user('sm_house_b02', 'smoke_detector')


    items = [(k, v) for k, v in dcontrols.items() if k in lctrls]

    print('items', items)

    need_change = False
    # items_send = []
    for i, e in enumerate(items):
        if e != items_old[i]:
            # items_send += [e]
            need_change = True

    dcontrols2 = [{'name': k, 'value': v} for k, v in items]

    data = {
        "controllers": dcontrols2
    }

    res = 0
    if need_change:
        res = set_data(data)
    print(11, need_change)

if __name__ == "__main__":
    smart_home_manager()
