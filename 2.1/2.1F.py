name = input()
price_per_kg = int(input()) 
weight = int(input())
money = int(input())
total_price = weight * price_per_kg
print(f'''Чек
{name} - {weight}кг - {price_per_kg}руб/кг
Итого: {total_price}руб
Внесено: {money}руб
Сдача: {money - total_price}руб''')