# Problema dos parâmetros mutáveis em funções Python


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


# cliente1 = adiciona_clientes('Luiz')
# adiciona_clientes('Joana', cliente1)
# print(cliente1)

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente1)

lista1 = []
cliente1 = adiciona_clientes('Luiz', lista1)
adiciona_clientes('Joana', cliente1)
print(cliente1)