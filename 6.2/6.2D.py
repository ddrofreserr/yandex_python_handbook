import pandas as pd 


def cheque(price_list, **kwargs):
    ans = pd.DataFrame({
        'product': list(kwargs.keys()),
        'price': price_list[kwargs.keys()],
        'number': list(kwargs.values()),
        'cost': price_list[kwargs.keys()] * [int(num) for num in kwargs.values()]
                       }).sort_values(['product'])
    ans.index = range(len(kwargs))
    return ans


def discount(ch_to_check):
    new_ch = ch_to_check.copy()
    new_ch['cost'] = new_ch['cost'] / ((new_ch['number'] > 2) + 1)
    return new_ch
