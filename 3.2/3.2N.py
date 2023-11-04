recipe_book = {}

ingredients, available = set(), set()

for i in range(int(input())):
    ingredients.add(input())
for j in range(int(input())):
    dish = input()
    for k in range(int(input())):
        recipe_book[dish] = recipe_book.get(dish, []) + [input()]
    flag = True
    for each in recipe_book[dish]:
        if each not in ingredients:
            flag = False
            break
    if flag:
        available.add(dish)
if len(available) != 0:
    for to_cook in sorted(available):
        print(to_cook)
else:
    print('Готовить нечего')
