surs = {}
while stroke := input():
    window = stroke.split()
    for object in window:
        surs[object] = surs.get(object, 0) + 1
for key, val in surs.items():
    print(key, val)
