"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""

variavel_1 = 1


def soma(x: int | float, y: int | float) -> int | float:  # type annotations
    """
    Soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y


def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None,
) -> int | float:
    """Mutliplica x, y e/ou z

    Mutliplica x e y. Se z for enviado, mutiplica x, y e z.
    """
    if z is None:
        return x * y
    return x * y * z


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4