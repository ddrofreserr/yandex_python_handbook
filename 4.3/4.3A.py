def recursive_sum(*args):
    if isinstance(args[0], int):
        args = [each for each in args]
    else:
        args = args[0]
    if len(args) != 0:
        return recursive_sum(args[:-1]) + args[-1]
    else:
        return 0
