import sqlite3

from main import DB_FILE, TABLE_NAME

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# fetchall
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')

# fetchone
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)


cursor.close()
con.close()
