class NoSolutionsError(ArithmeticError):
    pass
 

class InfiniteSolutionsError(ArithmeticError):
    pass


def find_roots(a, b, c):
    if not all(isinstance(each, int) or isinstance(each, float) for each in [a, b, c]):
        raise TypeError('Вызвано исключение TypeError')
    elif a == b == c == 0:
        raise InfiniteSolutionsError('Вызвано исключение InfiniteSolutionsError')
    if a == 0 != b:
        return - c / b, - c / b
    D = b ** 2 - 4 * a * c
    if D < 0 or a == b == 0:
        raise NoSolutionsError('Вызвано исключение NoSolutionsError')
    root1 = (- b - D ** 0.5) / 2 * a
    root2 = (- b + D ** 0.5) / 2 * a
    return min(root1, root2), max(root1, root2)
