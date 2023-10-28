first_num = int(input())
second_num = int(input())
ans = ((first_num // 1000 + second_num // 1000) % 10) * 1000
ans += ((first_num // 100 + second_num // 100) % 10) * 100
ans += ((first_num // 10 + second_num // 10) % 10) * 10
ans += ((first_num + second_num) % 10)
print(ans)