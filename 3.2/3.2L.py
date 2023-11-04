N = int(input())
employees = {}
for i in range(N):
    last_name = input()
    employees[last_name] = employees.get(last_name, 0) + 1
flag = True
for last_name, pers in sorted(employees.items()):
    if pers > 1:
        print(last_name, '-', pers)
        flag = False
if flag:
    print('Таких нет')
