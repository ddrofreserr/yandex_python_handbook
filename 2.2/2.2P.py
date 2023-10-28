speed_pt = int(input())
speed_vs = int(input())
speed_tl = int(input())


def pretty_print(A, B, C):
    blank = ' '
    place = 'I'
    print(f'{blank:8}{A:^8}{blank:8}')
    print(f'{B:^8}{blank:8}{blank:8}')
    print(f'{blank:8}{blank:8}{C:^8}')
    print(f'{place*2:^8}{place:^8}{place*3:^8}')


if (speed_vs < speed_tl < speed_pt):
    pretty_print('Петя', 'Толя', 'Вася')
elif (speed_tl < speed_vs < speed_pt):
    pretty_print('Петя', 'Вася', 'Толя')
elif (speed_vs < speed_pt < speed_tl):
    pretty_print('Толя', 'Петя', 'Вася')
elif (speed_pt < speed_vs < speed_tl):
    pretty_print('Толя', 'Вася', 'Петя')
elif (speed_tl < speed_pt < speed_vs):
    pretty_print('Вася', 'Петя', 'Толя')
else:
    pretty_print('Вася', 'Толя', 'Петя')
