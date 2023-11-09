def gcd(*params):
    first = params.pop(0)
    for second in params:
        first, second = max(first, second), min(first, second) 
        while (first % second != 0) and 0 < second < first:
            first, second = second, first % second
        first = second
    return first
