"""
Entendendo os seus próprios módulos Python
O primeiro móduço executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O Python conhece a pasta onde o __main__ está e as pastats abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por padrão.
O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path.
"""
import aula154_m
from aula154_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
print(aula154_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula154_m.soma(2, 3))
