# os + shutil - Copiando arquivos com Python
# 1 - Vamos copiar arquivos de uma pasta para outra;
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar -> os.unlink
# Apagar diretório recursivamente -> shutil.rmtree
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova_Pasta')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files, in os.walk(PASTA_ORIGINAL):

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
