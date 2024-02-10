from requests import get

site = 'http://' + input()
response = get(site)
ans = 0
while response.text != '0':
    ans += int(response.text) 
    response = get(site)
print(ans)
