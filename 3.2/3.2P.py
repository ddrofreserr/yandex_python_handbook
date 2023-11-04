ans_set = set()
while stroke := input():
    window = stroke.split(' ')
    for i, object in enumerate(window):
        if object == 'зайка':
            if i > 0:
                ans_set.add(window[i - 1])
            if i < len(window) - 1:
                ans_set.add(window[i + 1]) 
print(*ans_set, sep='\n')
