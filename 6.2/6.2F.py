def best(jou):
    return jou.copy()[jou['maths'] > 3][jou['physics'] > 3][jou['computer science'] > 3]
