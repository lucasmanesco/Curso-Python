from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    # nome: str = 'Missing.'
    nome: str = field(
        default='MISSING',
        repr=False,
    )
    sobrenome: str = 'Not sent.'
    idade: int = 0
    # enderecos: list[str] = []
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    print(p1)
