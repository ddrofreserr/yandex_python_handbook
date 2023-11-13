def make_linear(lists):
    ans = []
    for each in lists:
        if isinstance(each, list):
            ans += make_linear(each)
        else:
            ans += [each]
    return ans
