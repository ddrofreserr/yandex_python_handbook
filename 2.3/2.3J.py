y, x = 0, 0
while (direction := input()) != 'СТОП':
    steps = int(input())
    if direction == 'СЕВЕР':
        y += steps
    elif direction == 'ЮГ':
        y -= steps
    elif direction == 'ВОСТОК':
        x += steps
    else:
        x -= steps 
print(y, '\n', x, sep='')
