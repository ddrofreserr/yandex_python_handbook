first = input()
second = input()
third = input()
some = [first, second, third]
ans = [each for each in some if 'зайка' in each]
ans.sort()
print(ans[0], len(ans[0]))