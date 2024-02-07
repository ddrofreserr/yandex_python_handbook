import pandas as pd 
import numpy as np


def values(func, start, end, step):
    return pd.Series(func(np.arange(start, end + step, step)), index=np.arange(start, end + step, step))


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()
