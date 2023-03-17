"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos.
Faça em arquivos separados.
"""
import json


def save(my_list, file_path):
    data = my_list
    with open(file_path, 'w', encoding='utf8') as file:
        data = json.dump(my_list, file, indent=2, ensure_ascii=False)
    return data


FILE_PATH = 'aula206.json'


class Carro:
    def __init__(self, modelo, marca, ano, cor, motor, combustivel):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.combustivel = combustivel


c1 = Carro(
    'Fox',
    'Volkswagen',
    '2015',
    'Azul',
    '1.6 iMotion',
    'Flex'
)

save(vars(c1), FILE_PATH)
