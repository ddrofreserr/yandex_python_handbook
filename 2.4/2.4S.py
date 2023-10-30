N = int(input())
for i in range(1, N + 1):
    stroke = []
    for j in range(1, N + 1):
        stroke.append(min(min(i, j), min(N - i + 1, N - j + 1)))
    print(*stroke)
