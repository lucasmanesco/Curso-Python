# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html

# errors are cool! :)


def non_zeros(d):
    if d == 0:
        raise ZeroDivisionError('You are trying to divide by zero.')
    return True


def mustbe_int_float(n):
    type_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'"{n}" must be int or float.',
                        f'{type_n.__name__} not accepted.')
    return True


def divide (n, d):
    mustbe_int_float(n)
    mustbe_int_float(d)
    non_zeros(d)
    return n / d


print(divide(8, 'a'))
