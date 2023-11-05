from itertools import product

suits = {
    'буби': 'бубен',
    'пики': 'пик',
    'трефы': 'треф', 
    'черви': 'червей'
}


def insp(trio):
    if trio[0] == trio[2] and trio[1] == trio[3]:
        return False
    elif trio[0] == trio[4] and trio[1] == trio[5]:
        return False
    elif trio[2] == trio[4] and trio[3] == trio[5]:
        return False
    else:
        return True


nom = [str(i) for i in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
suit = input()
nom.remove(input())
nom.sort()

count = 0
for trio in product(nom, suits.values(), repeat=3):
    if suits[suit] in trio and insp(trio):
        if count < 10:
            print(f'{trio[0]} {trio[1]}, {trio[2]} {trio[3]}, {trio[4]} {trio[5]}')
            count += 1
