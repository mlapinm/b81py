import requests
import subprocess


def start():
  reqs = [
    ["/template/echo/?a=1", 'get'],
    ["/template/echo/?c=1", 'get'],
    ["/template/echo/", 'get'],
    ["/template/echo/", 'post'],  # 3
  ]
  url = "http://127.0.0.1:8000"
  num = 3
  for i in range(num, num + 1):
    req = reqs[i]
    if req[1] == 'get':
      res = requests.get(url + req[0], headers={'X-Print-Statement': 'test'})
    elif req[1] == 'post':
      res = requests.post(url + req[0], data={'bc': 1}, headers={'X-Print-Statement': 'test'})
      pass

    print(res.text)
    print(req, res.status_code)

if __name__ == "__main__":
  start()



