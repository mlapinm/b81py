
import json
from wsgiref import headers
import requests
import base64

from requests.auth import HTTPBasicAuth

url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'

name = 'alladin'
password = 'opensame'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

session = requests.Session()
session.get(url, headers=headers)
session.headers.update(headers)
Auth = base64.b64encode('LOGIN:PASSWORD'.encode('utf-8')).decode('utf-8')


resp = None
# resp = requests.post(url, headers = {'Authorization': 'Basic {}'.format(np)})
resp and print(resp.request.headers['Authorization'])
resp and print(resp.text)
# print(resp)
s = b"'{grade:42,feedback:hello}'".decode()
j = None
j = json.loads(s)
print(s)
print(j)


