from itertools import product

N, M = int(input()), int(input())
stroke = ''
max = len(str(N * M)) + 1
for i, j in product(range(0, N), range(1, M + 1)):
    stroke += f'{i * M + j :> {max}}'
    if len(stroke) == M * max:
        print(stroke[1:])
        stroke = ''
