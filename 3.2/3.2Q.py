friends = {}
while (record := input()):
    listed = record.split(' ')
    friends[listed[0]] = friends.get(listed[0], []) + [listed[1]]
    friends[listed[1]] = friends.get(listed[1], []) + [listed[0]]
friends_second = {key: set(val) for key, val in friends.items()}
for key, val in friends.items():
    for friend in val:
        ans = friends_second[key] | set(friends[friend]) - set([key])
        friends_second[key] = friends_second[key] | set(friends[friend]) - set([key])
    friends_second[key] = friends_second[key] - set(val)


friends_second = dict(sorted(friends_second.items()))
for k, v in friends_second.items():
    stroke = k + ': '
    for name in sorted(set(v)):
        if name != k:
            stroke += name + ', '
    print(stroke.strip(', '))
    