import requests

def get_data():
  url = 'http://smarthome.webpython.graders.eldf.ru/api/user.controller'
  headers = {"Authorization": "Bearer ce7b25df7e3b6b62379be94ebd6918190ad4544222b4de39cb963fb2162e5e6f"}

  resp = requests.get(url, headers=headers)
  data = resp.json()['data'][0]
  return data

if __name__ == "__main__":
  data = get_data()
  print(data)


