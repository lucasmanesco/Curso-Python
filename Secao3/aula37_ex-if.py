p1 = int(input('Digite valor 1: '))
p2 = int(input('Digite valor 2: '))

if p1 > p2:
    print(f'O primeiro valor ({p1}) é maior do que o segundo valor ({p2}).')
elif p2 > p1:
    print(f'O segundo valor ({p2}) é maior do que o primeiro valor ({p1}).')
else:
    print(f'Os valores são iguais. {p1} = {p2}.')
