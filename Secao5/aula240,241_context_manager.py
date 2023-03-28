# Context Manager com classes
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito relacionado
# com tipagem dinâmica onde o Python não está interessado
# no tipo, mas se alguns métodos existem no seu objeto
# para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um passáro que caminha como um pato,
# nada como um pato e grasna como um pato, eu chamo aquele
# pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e
# traceback. Se ele retornar True, exceção no with será suprimidas.

# Ex.:
# with open('aula240.txt', 'w') as file:
#     ...

class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening file...')
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file...')
        self._file.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # exception_.add_note('My note...')

        raise ConnectionError('Could not connect...')

        # return True  # tratei a exceção


with MyOpen('aula240.txt', 'w') as file:
    file.write('Line1\n')
    file.write('Line2\n', 123)
    file.write('Line3\n')
    print('WITH', file)
