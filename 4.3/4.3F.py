def merge_sort(numbers): 
    size = len(numbers)

    while size > 2:
        return merge(merge_sort(numbers[size // 2:]), merge_sort(numbers[:size // 2]))
    
    if size == 1:
        return numbers
    
    else:
        if numbers[0] > numbers[1]:
            return [numbers[1], numbers[0]]
        else:
            return numbers
        

def merge(list1, list2):
    ans = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] > list2[0]:
            ans.append(list2.pop(0))
        else:
            ans.append(list1.pop(0))
    ans += list2 + list1
    return ans
