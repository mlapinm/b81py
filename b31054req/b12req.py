
import requests
from requests.auth import HTTPBasicAuth 
import json

url = 'http://127.0.0.1:8000/api/v1/goods/'

name = 'alibaba'
password = '40razboinikov'
data = {
    "title": "Сыр \"Российский\"",
    "description": "Очень вкусный сыр, да еще и российский.",
    "price": 100
}
data2 = {
    "title": "Cheese",
    "description": "Good",
    "price": 100,
}

resp = requests.post(
    url, 
    data=json.dumps(data)
)

print(resp)
data = json.loads(resp.text)
print(data)


