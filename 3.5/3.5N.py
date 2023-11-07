from sys import stdin
import json


def update(dict_f, dict_s):
    for k, v in dict_s.items():
        if k in dict_f.keys():
            dict_f[k] = max(dict_f[k], dict_s[k])
        else:
            dict_f[k] = v


file_users_name = input()
data_merge = {}

with open(file_users_name, encoding="UTF-8") as file_users:
    data = json.load(file_users)
    for person in data:
        data_merge[person['name']] = {k: v for k, v in person.items() if k != 'name'}

with open(input(), encoding='UTF-8') as file_update:
    data_new = json.load(file_update)
    for person in data_new:
        update(data_merge[person['name']], {k: v for k, v in person.items() if k != 'name'})

with open(file_users_name, 'w', encoding="UTF-8") as file_users:
    json.dump(data_merge, file_users, indent=4)
