
import requests
import base64

from requests.auth import HTTPBasicAuth

url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'

name = 'alladin'
password = 'opensame'

resp = requests.post(
    url, auth = HTTPBasicAuth(
        name,
        password
    )
)
print(resp.request.headers['Authorization'])
print(resp.text)
print(resp)

