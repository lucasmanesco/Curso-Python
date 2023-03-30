# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas.
# Enums têm membros e seus valores são constantes.
# Enum em Python:
#     - São um conjunto de nomes simbólicos (membros) ligados a valores únicos
#     - Podem ser iterados para retornar seus membros canônicos na ordem de
#     definição.
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
# diretamente (mesmo assim, Enums não são classes normais em Python)
# Você poderá usar sseu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# chave = Classe,chave.name, Classe(valor), Classe['chave']
# valor = Classe.chave. value
import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum):
    # ESQUERDA = 1
    # DIREITA = 2
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    # if direcao not in ['esquerda', 'direita']:
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada.')

    print(f'Movendo para {direcao.name} -> ({direcao.value}).')


# mover('esquerda')
# mover('direita')
# mover('frente')
# mover('trás')
# mover('lado')
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
