product = input()
price_per_kg = int(input()) 
weight = int(input())
cash = int(input())

total_price = weight * price_per_kg
price_stroke = f'{weight}кг * {price_per_kg}руб/кг'
print(16 * '=' + 'Чек' + 16 * '=', sep='')
print(f'Товар: {product:>28}', sep='')
print(f'Цена: {price_stroke:>29}', sep='')
print(f'Итого: {total_price:>25}руб', sep='')
print(f'Внесено: {cash:>23}руб', sep='')
print(f'Сдача: {cash - total_price:>25}руб', sep='')
print(35 * '=')