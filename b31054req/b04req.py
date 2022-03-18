
# https://qna.habr.com/q/919711
# https://docs-python.ru/packages/modul-requests-python/autentifikatsija-modulem-requests/

import requests
import base64

url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
name = 'alladin'
password = 'opensame'

resp = requests.post(
    url, auth = (
        base64.b64encode(name.encode()),
        base64.b64encode(password.encode())
    )
)
print(resp.request.headers['Authorization'])
print(resp.text)
print(resp)