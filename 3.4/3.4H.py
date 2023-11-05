from itertools import islice, cycle

menu = []
for i in range(int(input())):
    menu.append(input())
for dish in islice(cycle(menu), int(input())):
    print(dish)
