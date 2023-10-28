num = int(input())
name = input()
for i in range(num - 1):
    if (new_name := input()) < name:
        name = new_name
print(name)
