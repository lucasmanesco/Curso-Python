# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__ - só sabe passar para o próximo

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))


print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)