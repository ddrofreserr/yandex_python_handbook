def fibonacci(num):
    n1, n2 = 0, 1
    for i in range(num):
        yield n1
        n1, n2 = n2, n1 + n2
