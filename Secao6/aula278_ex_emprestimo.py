# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela.
from datetime import datetime

from dateutil.relativedelta import relativedelta

data1 = '20/12/2022'
data_fmt = '%d/%m/%Y'

inicio_emprestimo = datetime.strptime(data1, data_fmt)
prazo = relativedelta(years=5)
fim_emprestimo = inicio_emprestimo + prazo

print(f'Início do empréstimo: {inicio_emprestimo.strftime(data_fmt)}.')
print(f'Fim do empréstimo: {fim_emprestimo.strftime(data_fmt)}.')

parcela = 0
emprestimo: float = 1_000_000
valor_parcela = emprestimo / 60

while inicio_emprestimo < fim_emprestimo:
    inicio_emprestimo += relativedelta(months=1)
    parcela += 1
    emprestimo -= valor_parcela
    print(f'Parcela {parcela}/60 - {inicio_emprestimo.strftime(data_fmt)}')
    print(f'Parcela: R${valor_parcela:,.2f} - Saldo: R${emprestimo:,.2f}')
    print(50 * '-')
