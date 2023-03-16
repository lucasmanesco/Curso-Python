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
*Rubber Duck Debugging*
"""


def listit(l):
    # guard clause
    if not l:
        print('No list to show.')
        return
    print('Tasks:')
    print(*l, sep='\n')


def add(item, l):
    l.append(item)
    return l


def undo(l, lr):
    # guard clause
    if not l:
        print('No action to do.')
        return
    removed = l.pop()
    lr.append(removed)


if __name__ == '__main__':
    print('To-Do List\n' 'Commands: List / Undo / Redo / Exit\n')
    to_do = []
    to_do_r = []

    while True:
        command = input('Type a task or command: ')
        print()

        if command.lower() == 'list':
            listit(to_do)
            print()

        elif command.lower() == 'undo':
            undo(to_do, to_do_r)
            listit(to_do)
            print()

        elif command.lower() == 'redo':
            undo(to_do_r, to_do)
            listit(to_do)
            print()

        elif command.lower() == 'exit':
            break

        elif command == '':
            print('You must type something.')
            print()

        else:
            add(command, to_do)
            listit(to_do)
            print()

print('Tks for using. =)')
