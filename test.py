a = 5
v = 10

print(a+v)

import requests
import pprint from pprint

def test_first():
    url = 'https://send-request.me/api/users'
    data = {
        'first_name': 'Georgianna',
        'last_name': 'Dickinson',
        'company_id': 1
    }
    response = requests.post(url, json = data)
    pprint (response.json())

print(a+v)
