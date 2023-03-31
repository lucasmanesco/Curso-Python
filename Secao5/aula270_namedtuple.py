# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros
# de bases de dados, etc.
# As namedtuples são imutáveis assim com as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple

# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'valor'
    naipe: str = 'naipe'


# Carta = namedtuple(
#       'Carta', ['valor', 'naipe'],
#       defaults=['valor', 'naipe']
# )

as_espadas = Carta('A', 'Espada')

print(as_espadas._asdict())
