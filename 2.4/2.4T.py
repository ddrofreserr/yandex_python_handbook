def base_prof(num, base):
    ben = 0
    while num > 0:
        ben += num % base
        num //= base
    return ben


N = int(input())
list = [base_prof(N, i) for i in range(2, 11)]
print(list.index(max(list)) + 2)
