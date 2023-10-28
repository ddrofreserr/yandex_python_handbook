num = list(input())
num += list(input())
new_num = [int(each) for each in num]
max_num = max(new_num)
min_num = min(new_num)
remain_num = (sum(new_num) - max_num - min_num) % 10
print(f'{max_num}{remain_num}{min_num}')
