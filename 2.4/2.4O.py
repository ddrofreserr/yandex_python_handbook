N = int(input())
M = int(input())
width = len(str(N * M))


for i in range(1, N + 1):
    stroke = ' ' * width + f'{i}' + ' ' * width
    for j in range(2, M + 1):
        stroke += '|' + ' ' * (width - len(str(i * j)) + 1) + f'{i * j}' + ' ' * width
    print(stroke)
    if i != N:
        print('-' * len(stroke))