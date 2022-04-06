import requests
from coursera_house.settings import SMART_HOME_API_URL, SMART_HOME_ACCESS_TOKEN

from django.core.mail import send_mail
from coursera_house.settings import EMAIL_RECEPIENT

def send_mail_user(subject, text):
    n = send_mail(subject, text, 'mlapin@rambler.ru', [EMAIL_RECEPIENT], fail_silently=True)
    return (n, EMAIL_RECEPIENT)


headers = {"Authorization": "Bearer {}".format(SMART_HOME_ACCESS_TOKEN)}


def get_data():
  url = SMART_HOME_API_URL

  global headers

  resp = requests.get(url, headers=headers)
  if resp.status_code != 200:
    text = '{}'.format(resp)
    send_mail_user('smart_home_b02', text)

  data = resp.json()['data']
  for e in data:
    if e['name'] == 'bedroom_light':
      # print(e['name'], e['value'])
      pass
  return data

def set_data(data):
  '''
  data = {
  "controllers": [
    {
      "name": "bedroom_light",
      "value": False
    }
  ]
  }
  '''

  url = SMART_HOME_API_URL
  global headers

  resp = requests.post(url, headers=headers, json=data)
  if resp.status_code != 200:
    text = '{}'.format(resp)
    send_mail_user('smart_home_b02', text)
  return resp


if __name__ == "__main__":
  data = ''
  data = set_data()
  # print(data)
  # print(data.text)
  data = get_data()
  
  
  # print(data)


