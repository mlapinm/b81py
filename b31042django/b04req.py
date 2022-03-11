import requests

if __name__ == "__main__":
  reqs = [
    "/index/",
    "/routing/simple_route/", # 200
    "/routing/simple_route/blabla", # 404 
    "/routing/simple_route/", # 405 post
    "/routing/simple_route/", # 405 put
    "",
    "",
  ]
  url = "http://127.0.0.1:8000"
  req = reqs[1]
  res = requests.get(url + req)
  print(res.text)
  print(res.status_code)
  req = reqs[3]
  res = requests.post(url + req, data={'key':'value'})
  print(res.text)
  print(req, res.status_code)
  res = requests.put(url + req, data={'key':'value'})
  print(res.text)
  print(req, res.status_code)


  # print(dir(requests))
  # print(help())


