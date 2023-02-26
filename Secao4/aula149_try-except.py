# Try, except

a = 18
b = 0

try:
    c = a / b

except ZeroDivisionError as e:  # Informar qual erro será tratado
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Variável b não foi definida.')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:  # Exception trata QUALQUER erro
    print('Erro desconhecido.')

print('Continuar')
