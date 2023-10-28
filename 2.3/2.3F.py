first = int(input())
second = int(input())
first, second = max(first, second), min(first, second)
while (first % second != 0) and 0 < second < first:
    first, second = second, first % second
print(second)
