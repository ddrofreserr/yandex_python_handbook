import json

stat = []
with open(input(), 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        if line != '\n':
            stat += [int(num) for num in line.rstrip('\n').split(' ')]
        
num = len(stat)
summa = sum(stat)
av = 0
if summa != 0:
    av = f'{summa / num :0.2f}'


stat = {"count": len(stat),
        "positive_count": len([i for i in stat if i > 0]),
        "min": min(stat),
        "max": max(stat),
        "sum": summa,
        "average": float(av)}


with open(input(), 'a', encoding='UTF-8') as file_json:
    json.dump(stat, file_json)
