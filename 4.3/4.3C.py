def make_equation(*args):
    if isinstance(args[0], int) or isinstance(args[0], str):
        args = [str(each) for each in args]
    else:
        args = args[0]
    if len(args) != 1:
        return "(" + make_equation(args[:-1]) + f') * x + {args[-1]}'
    else:
        return str(args[0])
