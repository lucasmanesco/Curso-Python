# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório autal (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('\\Users', 'Engenharia04', 'Downloads', 'dir_exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta aual:', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        print('  ', the_counter, 'File:', file_)

        # NÃO FAÇA ISSO, VAI APAGAR TUDO DA PASTA:
        # os.unlink(caminho...)
