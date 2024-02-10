from requests import get

res = get('http://' + input() + '/users').json()

for pers in sorted(res, key=lambda x: x['last_name']):
    print(pers['last_name'], pers['first_name'])
