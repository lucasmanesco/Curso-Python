# os.listdir para navegar em caminhos
import os

caminho = os.path.join('\\Users', 'Engenharia04', 'Downloads', 'dir_exemplo')

for pasta in os.listdir(caminho):

    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for arquivo in os.listdir(caminho_completo_pasta):
        print('  ', arquivo)
