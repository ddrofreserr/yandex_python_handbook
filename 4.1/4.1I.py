def is_prime(number):
    for i in range(1, int(number ** 0.5) + 1):
        if (number % i == 0 and i != 1) or number == 1:
            return False
    return True
