prev_h = 0
ans = -1
for i in range(int(input())):
    num = int(input())
    h = num % 256
    r = (num // 256) % 256
    m = num // 256 ** 2
    if h != 37 * (r + m + prev_h) % 256:
        ans = i
        break
    else:
        prev_h = h
print(ans)
