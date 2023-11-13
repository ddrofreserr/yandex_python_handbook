def recursive_digit_sum(num):
    if num != 0:
        return recursive_digit_sum(num // 10) + int(num % 10)
    else:
        return 0
