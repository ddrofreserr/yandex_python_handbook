set_f, set_s, set_t = set(), set(), set()
with open(input(), 'r', encoding='UTF-8') as file_f:
    for line in file_f.readlines():
        set_f = set_f | {word.rstrip('\n') for word in line.split(' ') if word != ''}

with open(input(), 'r', encoding='UTF-8') as file_s:
    for line in file_s.readlines():
        set_s = set_s | {word.rstrip('\n') for word in line.split(' ') if word != ''}

unique = set_f ^ set_s
with open(input(), 'w', encoding='UTF-8') as file_ans:
    for each in sorted(unique):
        file_ans.writelines(each + '\n')
