import json

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Manesco',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.75,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# https://www.youtube.com/watch?v=XmCrArtfjaQ

with open('aula190.json', 'w', encoding='utf8') as file:
    json.dump(pessoa,
              file,
              ensure_ascii=False,
              indent=2,
              )

with open('aula190.json', 'r', encoding='utf8') as file:
    pessoa2 = json.load(file)
    print(pessoa2)
    print(type(pessoa2))
    print(pessoa2['nome'])
