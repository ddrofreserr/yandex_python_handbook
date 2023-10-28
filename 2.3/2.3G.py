first_unmod = int(input())
second_unmod = int(input())
first, second = max(first_unmod, second_unmod), min(first_unmod, second_unmod)
while (first % second != 0) and 0 < second < first:
    first, second = second, first % second
print(first_unmod * second_unmod // second)
