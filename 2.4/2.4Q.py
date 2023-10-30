def pal(number_str):
    ans = True
    for i in range(len(number_str) // 2):
        if number_str[i] != number_str[-i - 1]:
            ans = False
    return ans


total = 0
for i in range(int(input())):
    ans = 1
    if pal(new := input()):
        total += ans
print(total)
