"""
Entendendo os seus próprios módulos Python
O primeiro móduço executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O Python conhece a pasta onde o __main__ está e as pastats abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por padrão.
O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path.
"""
try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...

import aula154_m

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
