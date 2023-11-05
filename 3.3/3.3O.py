from itertools import permutations

total = set()
for i in range(int(input())):
    total = total | {product for product in input().split(', ')}
for comb in permutations(sorted(total), 3):
    print(*comb)
