counter, stop = 1, 1
stroke, strokes = '', []
for i in range(N := int(input())):
    stroke += f'{i + 1}'
    if counter == stop or i + 1 == N:
        stop += 1
        counter = 1
        strokes.append(stroke)
        stroke = ''
    else:
        counter += 1
        stroke += ' '
max = len(strokes[- 1])
for stroke in strokes:
    print(f'{stroke:^{max}}')
