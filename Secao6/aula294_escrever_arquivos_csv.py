# csv.writer e csv.DictWriter

import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'aula294.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av. 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av. B, 3A'},
]

# with open(CSV_PATH, 'w') as file:
#     nome_colunas = lista_clientes[0].keys()
#     writer = csv.writer(file)

#     writer.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         writer.writerow(cliente.values())

with open(CSV_PATH, 'w') as file:
    nome_colunas = lista_clientes[0].keys()
    writer = csv.DictWriter(
        file,
        fieldnames=nome_colunas
    )
    writer.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        writer.writerow(cliente)
