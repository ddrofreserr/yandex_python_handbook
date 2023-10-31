def pal(number_str):
    ans = True
    for i in range(len(number_str) // 2):
        if number_str[i] != number_str[-i - 1]:
            ans = False
    return ans

    
stroke = input()
if pal(stroke.replace(' ', '').lower()):
    print('YES')
else:
    print('NO')