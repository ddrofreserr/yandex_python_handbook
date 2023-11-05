from itertools import product

letters = set()
stroke = input()
for char in stroke.split(' '):
    if char.isupper() and char.isalpha() and len(char) == 1:
        letters.add(char)

print(' '.join(sorted(letters)) + ' F')
for tup in product([0, 1], repeat=len(letters)):
    example = {char: var for char, var in zip(sorted(letters), tup)}
    F = eval(stroke, example)
    print(*tup, int(F))
