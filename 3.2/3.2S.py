kids = {}
for k in range(int(input())):
    new = [each.strip(':,') for each in input().split(' ')]
    kids[new[0]] = set(new[1:])
set_ans = set()
for key, val in kids.items():
    ans = val
    for key_compare, val_compare in kids.items():
        if key != key_compare:
            ans = ans - val_compare
    set_ans = set_ans | ans
for toy in sorted(set_ans):
    print(toy)
