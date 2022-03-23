import json
import requests
from requests.auth import HTTPBasicAuth 

def add_item_auth():

    url = "http://127.0.0.1:8000/api/v1/goods/"

    item_data = {
        "title": "aa",
        "description": "bbbb",
        "price": 99
    }

    name = 'hello'
    password = 'world'

    resp = requests.post(
        url, auth = HTTPBasicAuth(
            name,
            password
        ), json=item_data
    )


    # resp = requests.post(url, json=item_data)

    print(resp.text)
    print(resp)


def add_item():

    url = "http://127.0.0.1:8000/api/v1/goods/"

    item_data = {
        "title": "Сыр \"Российский\"",
        "description": "Очень вкусный сыр, да еще и российский.",
        "price": 99
    }

    data = json.dumps(item_data)
    resp = requests.post(url, data)

    print(resp.text)
    print(resp)



def add_review():

    url = "http://127.0.0.1:8000/api/v1/goods/3/reviews/"

    review_data = {
        "grade": 3,
        "text": "good good",
    }

    data = json.dumps(review_data)
    resp = requests.post(url, json=review_data)

    print(resp.text)
    print(resp)


if __name__ == "__main__":

    # add_item()
    # add_review()
    add_item_auth()


