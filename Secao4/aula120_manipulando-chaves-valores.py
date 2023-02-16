# Manipulando chaves em valores em dicionários

pessoa = {}

pessoa['nome'] = 'Lucas'
print(pessoa)
print(pessoa['nome'])


# chave dinâmica
chave = 'sobrenome'
pessoa[chave] = 'Manesco'
print(pessoa)

# apagar chave
del pessoa[chave]
print(pessoa[chave])

# get key
if pessoa.get('nome') is None:
    print('Não existe a chave.')
else:
    print(pessoa['nome'])
