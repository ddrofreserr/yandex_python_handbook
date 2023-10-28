num = int(input())
ans = 'YES'
for i in range(1, num // 2 + num % 2 + 1):
    if (num % i == 0 and i != 1) or num == 1:
        ans = 'NO'
        break
print(ans)
