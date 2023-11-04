prefs = {}
for i in range(int(input())):
    new = input().split()
    for kasha in new[1:]:
        prefs[kasha] = prefs.get(kasha, []) + [new[0]]
find = input()
if find in prefs.keys():
    print(*sorted(prefs[find]), sep='\n')
else:
    print('Таких нет')
