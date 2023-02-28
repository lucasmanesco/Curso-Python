"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funçoes decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções
decoradoreas em outras funções.
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, foi decorada.')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma string')


inverte_str_check_param = criar_funcao(inverte_string)
invertida = inverte_str_check_param('123')
print(invertida)
