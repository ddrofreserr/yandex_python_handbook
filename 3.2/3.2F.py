N, M = int(input()), int(input())
kids = set()
for i in range(N + M):
    kid = input()
    if kid in kids:
        kids.discard(kid)
    else:
        kids.add(kid)
if len(kids) == 0:
    print('Таких нет')
for kid in sorted(kids):
    print(kid)
