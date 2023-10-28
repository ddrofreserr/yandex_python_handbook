lengths = [int(input()), int(input()), int(input())]
validation = [each < sum(lengths) - each for each in lengths]
if sum(validation) == 3:
    print('YES')
else:
    print('NO')