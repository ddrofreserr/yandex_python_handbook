num = input()
ans = 'YES'
for i in range(len(num) // 2):
    if num[i] != num[-i - 1]:
        ans = 'NO'
        break
print(ans)
