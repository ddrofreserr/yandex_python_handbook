numbers = input().split(' ')
degree = int(input())
raised = [int(num) ** degree for num in numbers]
print(*raised)