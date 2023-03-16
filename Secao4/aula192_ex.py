"""
Exercício - Lista de Tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule thw world - Tears for Fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> adicionar fazer café
todo = ['fazer café', 'caminhar'] -> adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']

*Rubber Duck Debugging
"""


def listar(lista):
    print(*lista, sep='\n')


def adicionar(item, lista):
    lista.append(item)
    return lista


def desfazer():
    ...


def refazer():
    ...


if __name__ == '__main__':
    print('To-Do List\n' 'Comandos: Listar / Desfazer / Refazer / Sair\n')
    todo = []

    while True:
        comando = input('Digite uma tarefa/comando: ')
        print()

        if comando.lower() == 'listar':
            listar(todo)
            print()
        elif comando.lower() == 'desfazer':
            desfazer()
            listar(todo)
            print()
        elif comando.lower() == 'refazer':
            refazer()
            listar(todo)
            print()
        elif comando.lower() == 'sair':
            break
        else:
            adicionar(comando, todo)
            listar(todo)
            print()
