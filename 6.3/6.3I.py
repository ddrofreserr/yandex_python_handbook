from requests import put
from sys import stdin
from json import dumps

url = f'http://{input()}/users/{input()}'
new_data = dict()
for rec in stdin.read().split():
    field, new = rec.split('=')
    new_data[field] = new
req = put(url, data=dumps(new_data))
