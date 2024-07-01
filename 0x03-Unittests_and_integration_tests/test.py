import requests


url = "https://dog.ceo/api/breed/hound/list"

def get_dog(url):
    response = requests.get(url)
    body = response.json()
    print(type(body))
    print(body)
    return body


get_dog(url)