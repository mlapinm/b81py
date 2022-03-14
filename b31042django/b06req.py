import requests
import subprocess

def start():
  reqs = [
    "/index/",
    "/routing/simple_route/", # 200
    "/routing/simple_route/blabla", # 404 
    "/routing/simple_route/", # 405 post
    "/routing/simple_route/", # 405 put
    "/routing/slug_route/a-1s_d2/",
    "/routing/slug_route/.4/24][/",
    "/routing/sum_route/1/2/",
    "/routing/sum_route/1/-2/",
    "/routing/sum_route/1/b/",
    "/routing/sum_route/a/2/",
    "/routing/sum_get_method/",
    "/routing/sum_get_method/?a=1&b=-2",
    "/routing/sum_get_method/?a=1&b=b",
    "/routing/sum_get_method/",
    "/routing/sum_post_method/",
    "",
    "/routing/slug_route/y.m)*:;>?",
    "/routing/slug_route/aaaa",
    "/routing/slug_route/y.m)*:;>?",
    "/routing/sum_post_method/?a=7&b=87",
    "/template/echo/",
  ]
  url = "http://127.0.0.1:8000"
  num = 21 # 5 # 17
  for i in range(num, num + 1):
    req = reqs[i]
    if i == 3:
      res = requests.post(url + req, data={'key':'value'})
    elif i == 4:
      res = requests.put(url + req, data={'key':'value'})
    elif req == '/routing/sum_post_method/':
      res = requests.post(url + req, data={'a': '1', 'b': '2'})
      res = requests.post(url + req, data={})
    elif '/template/echo/' in req:
      res = requests.get(url + req, headers={'X-Print-Statement': 'test'})
      # res = requests.get(url + req)
    else:
      res = requests.get(url + req)

    print(res.text)
    print(req, res.status_code)

if __name__ == "__main__":
  start()
  # code = subprocess.call([
  # r"C:\python37\python", 
  # r"D:\avi02prog\b81env\b81py\b31042django\test.py"
  # ])



