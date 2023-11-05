from itertools import product

suits = ['пик', 'треф', 'бубен', 'червей']
lasts = ['валет', 'дама', 'король', 'туз']
suits.remove(input())
for nom, suit in product(range(2, 11), suits):
    print(nom, suit)
for nom, suit in product(lasts, suits):
    print(nom, suit)
