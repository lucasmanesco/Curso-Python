# Context Manager com função
# Criando e usando gerenciadores de contexo

from contextlib import contextmanager


@contextmanager
def my_open(path_file, mode):
    try:
        print('Opening file...')
        file = open(path_file, mode, encoding='utf8')
        yield file
    # except Exception as e:
    #     print('Error ocurred!', e)
    finally:
        print('Closing file...')
        file.close()


with my_open('aula242.txt', 'w') as file:
    file.write('Line1\n')
    file.write('Line2\n')
    file.write('Line3\n', 123)
    print('WITH', file)
