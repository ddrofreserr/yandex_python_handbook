stat = []
with open(input(), 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        if line != '\n':
            stat += [int(num) for num in line.rstrip('\n').split(' ')]
        
num = len(stat)
summa = sum(stat)
sredn = 0
if summa != 0:
    sredn = f'{summa / num :0.2f}'
print(num, len([i for i in stat if i > 0]), min(stat), max(stat), summa, sredn, sep='\n')
