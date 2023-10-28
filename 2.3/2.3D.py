first = int(input())
last = int(input())
ans = []
if first <= last:
    for i in range(first, last + 1):
        ans.append(i)
else:
    for i in range(first, last - 1, -1):
        ans.append(i)
print(*ans)
