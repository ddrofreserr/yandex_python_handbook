stroke = input().split(' ')
print('[')
for i, num in enumerate(stroke):
    bin_num = bin(int(num))[2:]
    new_num = '{' + f'''
        "digits": {len(bin_num)},
        "units": {bin_num.count('1')},
        "zeros": {bin_num.count('0')}
        ''' + '}'
    if i < len(stroke) - 1:
        new_num += ','
    print(new_num)
print(']')
