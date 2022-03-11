import requests

if __name__ == "__main__":
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
    "",
  ]
  url = "http://127.0.0.1:8000"
  num = 15
  for i in range(num, num + 1):
    req = reqs[i]
    if i == 3:
      res = requests.post(url + req, data={'key':'value'})
    elif i == 4:
      res = requests.put(url + req, data={'key':'value'})
    elif req == '/routing/sum_post_method/':
      res = requests.post(url + req, data={'a': 1, 'b': '2'})
    else:
      res = requests.get(url + req)

    print(res.text)
    print(req, res.status_code)



