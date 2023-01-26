"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listas valores
da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

lista = []

while True:

    opcao = input('Selecione uma opção:\n[I]nserir / [A]pagar / [L]istar\n').upper()

    if opcao == 'L':
        if len(lista) == 0:
            print('Lista vazia.')
        for i, nome in enumerate(lista):
            print(i, nome)

    elif opcao == 'A':
        item_apagar = int(input('Qual item deseja apagar? N°: '))
        try:
            lista.pop(item_apagar)
            print(f'Item {item_apagar} apagado com sucesso.')
        except:
            print('Item não encontrado.')

    elif opcao == 'I':
        item_inserir = input('Qual item deseja inserir? Item: ')
        lista.append(item_inserir)
    
    else:
        print('Opção inválida, digite novamente.')
