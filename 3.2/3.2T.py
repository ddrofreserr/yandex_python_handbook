def dels(number):
    ans = []
    for i in range(1, number + 1):
        if (number % i == 0 and i != 1) or number == 1:
            ans.append(i)
    return set(ans)


stroke = set([int(each) for each in input().split('; ')])
deviders = {}
for num in sorted(stroke):
    deviders[num] = dels(num)


for num in sorted(stroke):
    ans = str(num) + ' - '
    for num_compare in sorted(stroke):
        if num != num_compare and deviders[min(num, num_compare)] & deviders[max(num, num_compare)] == set():
            ans += f'{num_compare}, '
    if ans != str(num) + ' - ':
        print(ans[:-2])
