# Modulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# inteiro - import nome_modulo
# V: você tem o namespace do módulo
# D: nomes grandes
"""import sys
print(sys.platform)
sys.exit() # sair do programa
print(123)"""

# partes - from nome_modulo import objeto1, objeto2
# V: nomes pequenos
# D: sem o namespace do módulo
"""from sys import exit, platform
print(platform)
exit()"""

# alias 1 - import nome_modulo as apelido
"""import sys as s
sys = 'My system.'
print(s.platform)
s.exit()"""

# alias 2 - from nome_modulo import objeto as apelido
"""from sys import platform as pf, exit as ex
print(pf)
ex()"""

# V: você pode reservar nomes para seu código
# D: pode ficar fora do padrão de linguagem


# má prática - from nome_modulo import *
# V: importa tudo de um módulo
# D: importa tudo de um módulo
"""from sys import *
print(platform)
exit()"""
