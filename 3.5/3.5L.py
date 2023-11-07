stat = []
with open(input(), 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        stat.append(line.strip('\n'))


def define(num):
    count_odd, count_even = 0, 0
    for char in num:
        if int(char) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    if count_even > count_odd:
        return 'even'
    elif count_odd == count_even:
        return 'eq'
    else:
        return 'odd'
    
        
fir = open(input(), 'a', encoding='UTF-8')
sec = open(input(), 'a', encoding='UTF-8')
thir = open(input(), 'a', encoding='UTF-8')

for line in stat:
    str_fir = str_sec = str_thir = ''
    for num in line.split(' '):
        if define(num) == 'even':
            str_fir += num + ' '
        elif define(num) == 'odd':
            str_sec += num + ' '
        else:
            str_thir += num + ' '
    fir.writelines(str_fir + '\n')
    sec.writelines(str_sec + '\n')
    thir.writelines(str_thir + '\n')

fir.close()
sec.close()
thir.close()
