# PILARES DO POO
#   1 - Abstração;
#   2 - Herança
#   3 - Encapsulamento
#   4 - Polimorfismo
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = public
#         pode ser usado em qualquer lugar
#  _  (um underline) = protected
#         NÃO DEVE ser usado fora da classe ou subclasses.
#  __ (dois underlines) = private
#         "name mangling" (desfiguração de nomes) em Python
#          _NomeClasse__nomeattr_ou_method
#         só deve ser usado na classe em que foi declarado.


class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'Método público'

    def _metodo_protected(self):
        return '_Método_protected'

    def __metodo_private(self):
        return '_Método_private'


f = Foo()

# public
print(f.public)
print(f.metodo_publico())

# protected - não deveria funcionar mas o python permite
# porém fuciona por convenção pep8
print(f._protected)
print(f._metodo_protected())

# private - name manglind - desfiguração de nome
# print(f.__private)
print(f._Foo__private)
# print(f.__metodo_private())
print(f._Foo__metodo_private())
