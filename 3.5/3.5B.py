from sys import stdin

changes = []
for line in stdin:
    info = [kid for kid in line.rstrip("\n").split(' ')]
    changes += [int(info[2]) - int(info[1])]
print(round(sum(changes) / len(changes)))
