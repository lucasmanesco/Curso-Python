"""
Criando arquivos com Python

Open - abrir arquivo (pode ou não existir)
Modos:
r (leitura), w (escrita), x (criação)
a (escreve no final), b (binário),
t (modo texto), + (leitura e escrita)

Context Manager - with (abre e fecha)
Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Módulo os:
os.remove ou unlink - apaga arquivo
os.rename - renomeia arquivo

Módulo json:
json.dump - gera um arq json
json.load - carrega um arq json
"""

file_path = 'C:\\Users\\Engenharia04\\Downloads\\Curso_Python_Udemy\\'
# no windows utilizar barra dupla (\\) ou raw string (r') no path
file_path += 'aula186.txt'

# abrindo arquivo dessa forma, sempre precisa fechar
# file = open(file_path, 'w')
# file.close()

# abrindo dessa forma, fecha automaticamente:
with open(file_path, 'w+') as file:

    print(type(file))

    file.write('Linha 1\n')
    file.write('Linha 2\n')

    file.writelines(('Linha 3\n', 'Linha 4\n'))

    file.seek(0, 0) # move cursor para o topo do arquivo
    print(file.read())

    print('Readline...')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline())

    print('Readlines...')
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip())

print('*' * 50)

with open(file_path, 'r') as file:
    print(file.read())
