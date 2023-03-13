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
file_path += 'aula186.txt'

with open(file_path, 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')

with open(file_path, 'a') as file:
    file.write('Atenção - encoding windows 1252\n')


with open(file_path, 'a', encoding='utf8') as file:
    file.write('Atenção - encoding utf8\n')
