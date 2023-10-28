num = list(input())
new_num = [int(each) for each in num]
sum_to_compare = min(new_num) + max(new_num)
if sum_to_compare == (sum(new_num) - sum_to_compare) * 2:
    print('YES')
else:
    print('NO')