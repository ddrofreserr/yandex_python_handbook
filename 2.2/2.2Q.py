a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    print(f'{-c / b:.2f}')
elif a == b == 0:
    print('No solution')
elif a == c == 0:
    print(0.00)
else:
    D = b * b - 4 * a * c
    if D > 0:
        root_one = (- b + D ** 0.5) / (2 * a)
        root_two = (- b - D ** 0.5) / (2 * a)
        print(f'{min(root_one, root_two):.2f} {max(root_one, root_two):.2f}')
    elif D == 0:
        root = (- b) / (2 * a)
        print(f'{root:.2f}')
    else:
        print('No solution')