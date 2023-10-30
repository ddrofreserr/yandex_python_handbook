def prost(number):
    ans = True
    for i in range(1, number // 2 + number % 2 + 1):
        if (number % i == 0 and i != 1) or number == 1:
            ans = False
    return ans


num = int(input())
ans = []
for j in range(2, num // 2 + num % 2):
    new_num = num
    if prost(j):
        while new_num % j == 0:
            new_num //= j
            ans.append(j)
print(*ans, sep=' * ')
