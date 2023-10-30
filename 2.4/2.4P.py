N = int(input())
M = int(input())
width = len(str(N * M)) - 1


for i in range(1, N + 1):
    stroke = ' ' * width + f'{i :^3}' + ' ' * width
    for j in range(2, M + 1):
        stroke += '|' + ' ' * width + f'{i * j :^3}' + ' ' * width
    print(stroke)
    if i != N:
        print('-' * len(stroke))
