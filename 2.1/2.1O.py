N = int(input())
M = int(input())
T = int(input())
first_num = (N + ((M + T) // 60)) % 24
second_num = (M + T) % 60
print(f'{first_num:>02}:{second_num:>02}')
