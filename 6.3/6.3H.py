from requests import post
from json import dumps

site = input()

data = {'username': input(),
        'last_name': input(),
        'first_name': input(),
        'email': input()
        }

req = post(f'http://{site}/users', data=dumps(data))
