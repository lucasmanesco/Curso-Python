"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos.
Faça em arquivos separados.
"""
import json
from aula206a_ex_json_classe import FILE_PATH, Carro


def read(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('File does not exist.')
        exit()
    return data


c1 = Carro(*read(FILE_PATH))
print(vars(c1))
