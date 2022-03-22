import json
import requests

url = "http://127.0.0.1:8000/api/v1/goods/2/reviews/"



review_item = {
    "grade": 2,
    "text": "good",
}

data = json.dumps(review_item)
resp = requests.post(url, data)

print(resp.text)
print(resp)

