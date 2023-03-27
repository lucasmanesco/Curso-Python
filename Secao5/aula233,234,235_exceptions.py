# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da lingaugem.
# A recomendação da doc é herdar de Exception.
# https://docs.python/org/3/library/execpetions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


class MyError(Exception):
    ...


class OtherError(Exception):
    ...


def raise_error():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Note 1.')
    exception_.add_note('Note 2.')
    raise exception_


try:
    raise_error()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OtherError('Raising again...')
    exception_.add_note('Note 3.')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
