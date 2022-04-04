import requests

headers = {"Authorization": "Bearer ce7b25df7e3b6b62379be94ebd6918190ad4544222b4de39cb963fb2162e5e6f"}

def get_data():
  url = 'http://smarthome.webpython.graders.eldf.ru/api/user.controller'
  global headers

  resp = requests.get(url, headers=headers)
  data = resp.json()['data']
  for e in data:
    if e['name'] == 'bedroom_light':
      # print(e['name'], e['value'])
      pass
  return data

def set_data():
  url = 'http://smarthome.webpython.graders.eldf.ru/api/user.controller'
  global headers

  data = {
  "controllers": [
    {
      "name": "bedroom_light",
      "value": False
    }
  ]
  }
  resp = requests.post(url, headers=headers, json=data)
  return resp


if __name__ == "__main__":
  data = ''
  data = set_data()
  # print(data)
  # print(data.text)
  data = get_data()
  
  
  # print(data)


