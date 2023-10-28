N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

total_price = N * M
first_weight = (total_price - K2 * N) // (K1 - K2)
second_weight = N - first_weight
print(first_weight, second_weight)
