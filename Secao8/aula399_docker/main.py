# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,  # Cursor para retornar dicionários
)

# -----------------------------------------------------------------------------#
# CRIANDO TABELA
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # CUIDADO: ISSO LIMPA A TABELA!
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

# COMEÇO A MANIPULAR DADOS A PARTIR DAQUI:

# -----------------------------------------------------------------------------#
# Inserindo um valor usando placeholder e iterável:

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )

        # PREVENINDO SQL INJECTION:
        data1 = ('Lucas', 28)
        result = cursor.execute(sql, data1)

        # print(sql, data1)
        # print(result)  # result = numero de linhas afetadas
    connection.commit()

# -----------------------------------------------------------------------------#
# Inserindo um valor usando placeholder e dicionário:

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )

        # PREVENINDO SQL INJECTION:
        data2 = {
            "age": 32,
            "name": "João",
        }
        result = cursor.execute(sql, data2)

        # print(sql, data2)
        # print(result)  # result = numero de linhas afetadas
    connection.commit()

# -----------------------------------------------------------------------------#
# Inserindo vários valores usando placeholder e tupla de dicionários:

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )

        # PREVENINDO SQL INJECTION:
        data3 = (
            {"age": 34, "name": "Maria", },
            {"age": 17, "name": "Júlia", },
            {"age": 12, "name": "Carlos", },
        )
        result = cursor.executemany(sql, data3)  # type: ignore

        # print(sql, data3)
        # print(result)  # result = numero de linhas afetadas
    connection.commit()

# -----------------------------------------------------------------------------#
# Inserindo vários valores usando placeholder e tupla de tuplas:

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )

        # PREVENINDO SQL INJECTION:
        data4 = (
            ("Siri", 10),
            ("Cortana", 10),
        )
        result = cursor.executemany(sql, data4)  # type: ignore

        # print(sql, data4)
        # print(result)  # result = numero de linhas afetadas
    connection.commit()

# -----------------------------------------------------------------------------#
# Lendo valores com SELECT:

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.executemany(sql)  # type: ignore
        data5 = cursor.fetchall()

        for row in data5:
            print(row)

# -----------------------------------------------------------------------------#
# Lendo valores com SELECT + WHERE:

    with connection.cursor() as cursor:
        id_recebido = int(input('Digite um id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            # f'WHERE id = {id_recebido} '  # !!! SQL INJECTION !!!
            'WHERE id = %s '
        )

        cursor.execute(sql, id_recebido)  # type: ignore
        # print(cursor.mogrify(sql, id_recebido))
        data5 = cursor.fetchall()

        for row in data5:
            print(row)

# -----------------------------------------------------------------------------#
# DELETE (DELETE SEM WHERE É PERIGOSO!)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore

        for row in cursor.fetchall():
            print(row)

# -----------------------------------------------------------------------------#
# UPDATE (UPDATE SEM WHERE É PERIGOSO!)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s, '
            'WHERE id = %s'
        )
        cursor.execute(sql, ('Carlos', 20, 1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore

        for row in cursor.fetchall():
            print(row)

# -----------------------------------------------------------------------------#
