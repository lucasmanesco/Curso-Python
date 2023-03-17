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
import os
import json


def listit(l1):
    # guard clause
    if not l1:
        print('No list to show.')
        return
    print('Tasks:')
    print(*l1, sep='\n')


def add(item, l1):
    l1.append(item)
    return l1


def undo(l1, lr):
    # guard clause
    if not l1:
        print('No action to do.')
        return
    removed = l1.pop()
    lr.append(removed)


def read(l1, file_path):
    dados = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('File does not exist. Creating...')
        save(l1, file_path)
    return dados


def save(l1, file_path):
    dados = l1
    with open(file_path, 'w', encoding='utf-8') as file:
        dados = json.dump(l1, file, indent=2, ensure_ascii=False)
    return dados


FILE_PATH = 'aula195-to-do-list.json'
to_do = read([], FILE_PATH)
to_do_r = []
print('To-Do List\n' 'Commands: List / Undo / Redo / Exit\n')

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

    elif command.lower() == 'clear':
        os.system('cls')

    elif command == '':
        print('You must type something.')
        print()

    else:
        add(command, to_do)
        listit(to_do)
        print()

    save(to_do, FILE_PATH)

print('Tks for using. =)')
