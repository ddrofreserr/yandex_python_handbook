recipes = {'Эспрессо': {'coffee': 1},
           'Капучино': {'coffee': 1,
                        'milk': 3},
           'Макиато': {'coffee': 2,
                       'milk': 1},
           'Кофе по-венски': {'coffee': 1,
                              'cream': 2},
           'Латте Макиато': {'coffee': 1,
                             'milk': 2,
                             'cream': 1},
           'Кон Панна': {'coffee': 1,
                         'cream': 1},
           }


def order(*args):
    global in_stock
    for drink in args:
        needed = recipes[drink]
        result = [v <= in_stock[k] for k, v in recipes[drink].items()]
        if False not in result:
            for k, v in needed.items():
                in_stock[k] -= v
            return drink
    return 'К сожалению, не можем предложить Вам напиток'
