# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25', 
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5', 
    },
]

acertos = 0

for p in perguntas:
    print(f'Pergunta: {p["Pergunta"]}')

    for i, o in enumerate(p['Opções']):
        print(f'{i}) {o}')

    resposta = input('Escolha uma opção: ')
    
    if resposta == str(p['Opções'].index(p['Resposta'])):
        print('Resposta correta.\n')
        acertos += 1
    else:
        print('Resposta incorreta.\n')

print(f'Você acertou {acertos}/{len(perguntas)} perguntas.')
