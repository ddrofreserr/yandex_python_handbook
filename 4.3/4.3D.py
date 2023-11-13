def answer(f):

    def decorated(*args, **kwargs):

        return f'Результат функции: {f(*args, **kwargs)}'
    
    return decorated
