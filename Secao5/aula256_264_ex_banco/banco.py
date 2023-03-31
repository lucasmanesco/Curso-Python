import contas
import pessoa


class Banco():
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _autentica_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_autentica_agencia', True)
            return True
        print('_autentica_agencia', False)
        return False

    def _autentica_conta(self, conta):
        if conta in self.contas:
            print('_autentica_conta', True)
            return True
        print('_autentica_conta', False)
        return False

    def _autentica_cliente(self, cliente):
        if cliente in self.clientes:
            print('_autentica_cliente', True)
            return True
        print('_autentica_cliente', True)
        return False

    def _autentica_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_autentica_conta_cliente', True)
            return True
        print('_autentica_conta_cliente', False)
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self._autentica_agencia(conta) and \
            self._autentica_conta(conta) and \
            self._autentica_cliente(cliente) and \
            self._autentica_conta_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

# --------------------------------------------------------------------------- #


if __name__ == '__main__':

    c1 = pessoa.Cliente('Lucas', 28)
    cc1 = contas.ContaCorrente(1234, 123456, 0, 0)
    c1.conta = cc1

    c2 = pessoa.Cliente('Jéssica', 26)
    cp1 = contas.ContaPoupanca(5678, 789012, 100)
    c2.conta = cp1

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([1234, 5678])

    print(banco.autenticar(c1, cc1))

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
