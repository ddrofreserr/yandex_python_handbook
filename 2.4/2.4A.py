num = int(input())
for i in range(1, num + 1):
    stroke = []
    for j in range(1, num + 1):
        stroke.append(i * j)
    print(*stroke)
