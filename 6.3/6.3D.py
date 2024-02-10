from requests import get

res = get("http://" + input()).json()
try:
    print(res[find := input()])
except KeyError:
    print('No data')
