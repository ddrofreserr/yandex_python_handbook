from hashlib import sha256


class MinLengthError(Exception):
    pass
 

class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, 
                        possible_chars='abcdefghijklmnopqrstuvwxyz1234567890_', at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError('Вызвано исключение TypeError')
    if len(password) < min_length:
        raise MinLengthError('Вызвано исключение MinLengthError')
    if not all(sym in possible_chars for sym in password.lower()):
        raise PossibleCharError('Вызвано исключение PossibleCharError')
    if not bool(sum(at_least_one(sym) for sym in password)):
        raise NeedCharError('Вызвано исключение NeedCharError')
    return sha256(bytes(password, 'UTF-8')).hexdigest()
