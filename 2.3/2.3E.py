total_price = 0
while (price := float(input())) != 0:
    total_price += (price - price * (price >= 500) / 10)
print(total_price)
