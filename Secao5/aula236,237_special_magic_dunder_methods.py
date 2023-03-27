# Python Special, Magic e Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods
# https://docs.python.org/3/reference/datamodel.html#sepcialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - - self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # para devs:
    def __repr__(self):
        # class_name = self.__class__.__name__, ou:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    # para retornar str:
    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(p1)  # __str__
print(p2)  # __str__
print(repr(p1))
print(repr(p2))
print(f'{p2!r}')
