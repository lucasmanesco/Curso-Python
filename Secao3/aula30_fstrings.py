nome = 'Lucas Manesco'
altura = 1.75
peso = 70

imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'kg e seu IMC é de', imc)

# f-strings
print(f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f}kg e seu IMC é de {imc:.2f}.')
