set_can, set_done = set(), set()
for i in range(int(input())):
    set_can.add(input())
for j in range(int(input())):
    for k in range(int(input())):
        set_done.add(input())
if len(set_can - set_done) != 0:
    for dish in sorted(set_can - set_done):
        print(dish)
else:
    print('Готовить нечего')
 