import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# CUIDADO: fazendo delete sem where -------------------------------------------
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
con.commit()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# criando tabela --------------------------------------------------------------
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
con.commit()

# registrar valores nas colunas da tabela -------------------------------------
# CUIDADO: sql injection
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight) '
#     'VALUES '
#     '(NULL, "Lucas Manesco", 67.5), (NULL, "Jéssica Sousa", 58.5'
# )
# con.commit()

# registrar com executemany ---------------------------------------------------
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)

cursor.executemany(
    sql,
    (
        ['Joana', 4], ['Luis', 5]
    )
)
con.commit()
print(sql)

# registrar com dicionarios ---------------------------------------------------
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

cursor.execute(sql, {'nome': 'José', 'peso': 4})
con.commit()
print(sql)

# registrar com executemany e dicionarios -------------------------------------
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

cursor.executemany(sql, (
    {'nome': 'José', 'peso': 1},
    {'nome': 'João', 'peso': 2},
    {'nome': 'Pedro', 'peso': 3},
))
con.commit()
print(sql)

# fechar ----------------------------------------------------------------------
cursor.close()
con.close()
