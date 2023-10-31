def nod(first, second):
    first, second = max(first, second), min(first, second) 
    while (first % second != 0) and 0 < second < first:
        first, second = second, first % second
    return second


stroke = input().split(' ')
compare = int(stroke[0])
for each in stroke[1:]:
    nod_num = nod(compare, int(each)) 
    compare = nod_num
print(nod_num)