def gcd(first, second):
    first, second = max(first, second), min(first, second)
    while (first % second != 0) and 0 < second < first:
        first, second = second, first % second
    return second


num = int(input())
first = int(input())
for i in range(num - 1):
    nod_num = gcd(first, int(input()))
    first = nod_num
print(nod_num)
