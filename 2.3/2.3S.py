def mean(first, second):
    if (first - second) == 1:
        return 1
    else:
        return (first - second) // 2


it_max = 1001
it_min = -1
attempt = 500
print(attempt)
while (hint := input()) != 'Угадал!':
    if hint == 'Больше':
        it_min = attempt
        attempt += mean(it_max, it_min)
    else:
        it_max = attempt
        attempt -= mean(it_max, it_min)
    print(attempt)
