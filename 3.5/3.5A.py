from sys import stdin

numbers = []
for line in stdin:
    numbers += [int(i) for i in line.rstrip("\n").split(' ')]
print(sum(numbers))
