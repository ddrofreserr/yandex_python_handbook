from requests import get

res = get("http://" + input()).json()
ans = 0
for val in res:
    if type(val) is int or type(val) is float:
        ans += val
print(ans)
