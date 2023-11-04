def RLE(stroke):
    ans, char = 1, stroke[0]
    for each in stroke[1:]:
        if each == char:
            ans += 1
        else:
            print(char, ans)
            ans = 1
            char = each
    return char, ans


print(*RLE(input()))
