"""
super() é a super classe na sub classe
Classe principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class
"""


# class MinhaString(str):
#     def upper(self):
#         print('Chamou .upper()')
#         retorno = super().upper()
#         print('Depois do upper.')
#         return retorno


# string = MinhaString('Lucas')
# print(string.upper())


class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei o sistema!')

    def metodo(self):
        super().metodo()  # B (super() = super(C, self))
        super(B, self).metodo()  # A
        super(A, self).metodo()  # object
        print('C')


c = C('atributo', 'Qualquer')
print(c.outra_coisa)
print(c.atributo)

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

# c.metodo()

print(C.mro())
print(B.mro())
print(A.mro())
