# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b',
    '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,  # Tipo do argumento
    metaver='STRING',
    # default='Olá mundo',  # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+'  # Recebe mais de um valor
)

args = parser.parse_args()
# print(args.b)

if args.basic is None:
    print('Você não passou o valor de basic.')
else:
    print('O valor de basic:', args.b)
