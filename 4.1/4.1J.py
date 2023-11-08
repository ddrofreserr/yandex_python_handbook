def merge(tup1, tup2):
    ans = []
    list1, list2 = list(tup1), list(tup2)
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] > list2[0]:
            ans.append(list2.pop(0))
        else:
            ans.append(list1.pop(0))
    ans += list2 + list1
    return tuple(ans)
