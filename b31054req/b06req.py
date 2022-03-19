
import requests
import json

from requests.auth import HTTPBasicAuth 

url = 'http://datasend.webpython.graders.eldf.ru/submissions/1/'

name = 'alladin'
password = 'opensesame'

resp = requests.post(
    url, auth = HTTPBasicAuth(
        name,
        password
    )
)
print(resp.request.headers['Authorization'])
print(resp.text)
with open('aa.txt', 'w', encoding='utf-8') as f:
    f.write(resp.text)
text = resp.text    
print(resp)

data = json.loads(text)
print(data)
