class BadCharacterError(Exception):
    pass
 

class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass
 

class CapitalError(Exception):
    pass


def cyrillic(text):
    for sym in text.lower():
        if sym not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            return False
    return True 
    

def goodchar(text):
    for sym in text.lower():
        if sym not in 'abcdefghijklmnopqrstuvwxyz1234567890_':
            return False
    return True


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not cyrillic(name):
        raise CyrillicError
    if name.capitalize() != name:
        raise CapitalError
    return name


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError('Вызвано исключение TypeError')
    if not goodchar(name):
        raise BadCharacterError('Вызвано исключение BadCharacterError')
    if name[0].isdigit():
        raise StartsWithDigitError('Вызвано исключение StartsWithDigitError')
    return name


def user_validation(**kwargs):
    if all(sm not in list(kwargs.keys()) for sm in ['last_name', 'first_name', 'username']) or len(kwargs.keys()) != 3:
        raise KeyError('Вызвано исключение KeyError')
    last_name, first_name, username = kwargs['last_name'], kwargs['first_name'], kwargs['username']
    if all(not isinstance(some, str) for some in (last_name, first_name, username)):
        raise TypeError('Вызвано исключение TypeError')
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    return {'last_name': last_name, 'first_name': first_name, 'username': username}
