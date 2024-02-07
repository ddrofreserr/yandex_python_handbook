import pandas as pd 


def length_stats(phrase):
    phrase = ''.join(ch for ch in phrase.lower() if ch.isalpha() or ch == ' ')
    phrase = sorted(set(phrase.split()))
    return pd.Series(map(len, phrase), index=phrase)
