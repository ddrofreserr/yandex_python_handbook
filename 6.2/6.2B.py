import pandas as pd 


def length_stats(phrase):
    phrase = ''.join(ch for ch in phrase.lower() if ch.isalpha() or ch == ' ')
    phrase = sorted(set(phrase.split()))
    ans = pd.Series([len(word) for word in phrase], index=phrase)
    return ans[ans % 2 != 0], ans[ans % 2 == 0]
