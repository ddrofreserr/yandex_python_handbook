def secret_replace(phrase, **kwargs):
    ans = list(phrase)
    for k, v in kwargs.items():
        while k in ans:
            for sym in v:
                if k in ans:
                    ans[ans.index(k)] = sym
    return ''.join(ans)
