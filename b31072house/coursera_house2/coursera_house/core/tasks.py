from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Setting
from .b02req import get_data, set_data

@task()
def smart_home_manager():
    controls = get_data()
    dcontrols = {}
    for e in controls:
        dcontrols[e['name']] = e['value']
    objs = Setting.objects.all()
    for e in objs:
        print(22, e.controller_name, e.value)
        pass

    if dcontrols['leak_detector'] == True:  # 1
        dcontrols['cold_water'] = False
        dcontrols['hot_water'] = False


    print(dcontrols)
    # Здесь ваш код для проверки условий
    pass
