from requests import get
from sys import stdin

site = "http://" + input()
ans = 0
paths_list = [path.strip() for path in stdin]
for path in paths_list:
    ans += sum(get(site + path).json())
print(ans)
