num = list(input())
new_num = [int(each) for each in num]
max_num = max(new_num)
min_num = min(new_num)
remain_num = sum(new_num) - max_num - min_num
if min_num == 0:
    print(f'{remain_num}{min_num} {max_num}{remain_num}')
else:
    print(f'{min_num}{remain_num} {max_num}{remain_num}')