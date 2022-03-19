
import requests
from requests.auth import HTTPBasicAuth 

url = 'http://datasend.webpython.graders.eldf.ru/submissions/secretlocation/'

name = 'alibaba'
password = '40razboinikov'

resp = requests.put(
    url, auth = HTTPBasicAuth(
        name,
        password
    ),
    data={"answer": "w3lc0m370ch4p73r4.2"}
)

print(resp)
print(resp.text)
ans = {"answer": "w3lc0m370ch4p73r4.2"}

