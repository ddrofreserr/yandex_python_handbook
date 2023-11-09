first_half, second_half = [], []


def enter_results(*args):
    global first_half, second_half
    first_half += [val for i, val in enumerate(args) if i % 2 == 0]
    second_half += [val for i, val in enumerate(args) if i % 2 == 1]


def get_sum():
    return round(sum(first_half), 2), round(sum(second_half), 2)


def get_average():
    return tuple([round(each / len(first_half), 2) for each in get_sum()])
