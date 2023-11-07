from sys import stdin
import json

file_name = input()

with open(file_name, encoding="UTF-8") as file_in:
    data = json.load(file_in)
    for line in stdin:
        if line != '':
            pair = line.rstrip('\n').split(' == ')
            data[pair[0]] = pair[1]

with open(file_name, 'w', encoding="UTF-8") as file_update:
    json.dump(data, file_update, ensure_ascii=False, indent=2)
