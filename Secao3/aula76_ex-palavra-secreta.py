"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a a letra
digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra.
    - Se a letra digitava não estiver na palavra secreta,exiba '*'.
- Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = 'Python'.lower()
acertos = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ').lower()
    tentativas += 1

    if letra.isalpha() and len(letra) <= 1:
        
        if letra in palavra_secreta:
            acertos += letra
            
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in acertos:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
    
        print('Palavra formada: ', palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print(f'Parabéns! Você acertou com {tentativas} tentativas.')
            break
                
    else:
        print('Digite uma letra: ')