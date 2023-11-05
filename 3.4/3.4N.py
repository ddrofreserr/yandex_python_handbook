from itertools import permutations

sporters = [input() for i in range(int(input()))]
for comb in permutations(sorted(sporters), 3):
    print(*comb, sep=', ')
