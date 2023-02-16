"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna um cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Manesco',
    # 'idade' : 28
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault('idade', 18)
print(pessoa['idade'])