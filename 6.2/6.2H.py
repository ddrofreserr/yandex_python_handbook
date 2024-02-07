def update(jou):
    new_jou = jou.copy()
    new_jou['average'] = (new_jou['maths'] + new_jou['physics'] + new_jou['computer science']) / 3
    return new_jou.sort_values(['average', 'name'], ascending=[False, True])
