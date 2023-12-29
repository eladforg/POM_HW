import requests


def test_cat():
    response=requests.get("https://catfact.ninja/fact")
    response_body=response.json()
    # print(response_body)


