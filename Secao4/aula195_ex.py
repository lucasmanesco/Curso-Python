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


def read(l, file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('List file not found. Creating...')
        save(l, file_path)
    return data


def save(l, file_path):
    data = l
    with open(file_path, 'w', encoding='utf8') as file:
        data = json.dump(l, file, ensure_ascii=False, indent=2)
    return data


FILE_PATH = 'aula195-to_do_list.json'
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
