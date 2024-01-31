def merge(a, b):
    if not hasattr(a, '__iter__') or not hasattr(b, '__iter__'):
        raise StopIteration
    elif notsametype(a) or notsametype(b) or type(a[0]) is not type(b[0]):
        raise TypeError
    elif sorted(a) != a or sorted(b) != b:
        raise ValueError
    else:
        ans = []
        while len(a) != 0 and len(b) != 0:
            if a[0] > b[0]:
                ans.append(b.pop(0))
            else:
                ans.append(a.pop(0))
        ans += b + a
        return ans


def notsametype(obj):
    for every in obj:
        if type(every) is not type(obj[0]):
            return True
