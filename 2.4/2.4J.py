num = int(input())
print('А Б В')
for i in range(1, num - 1):
    for j in range(1, num - 1):
        if num - (j + i) > 0:
            list = [i, j, num - (j + i)]
            print(*list)
