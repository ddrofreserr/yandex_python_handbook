def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    elif a % 2 != 0 or b % 2 != 0 or a + b <= max(a, b):
        raise ValueError
    else:
        return a + b
    