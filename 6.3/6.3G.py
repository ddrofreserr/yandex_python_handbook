from requests import get
from sys import stdin

site = input()
user_id = int(input())
res = get(f'http://{site}/users/{user_id}')
message = stdin.read()

if res.status_code != 200: 
    print('Пользователь не найден') 
else: 
    res = res.json() 
    print(message.format(**res))
