import sqlite3

conn = sqlite3.connect('ServerStorage.db')

conn.execute('drop table OPEN_KEYS')
conn.execute('drop table MESSAGES')  # message types: message; key-sharing

conn.execute('create table OPEN_KEYS (username text UNIQUE, openkey_x real, openkey_y real)')
conn.execute('create table MESSAGES (to_username text, from_username text, message text)')
c = conn.cursor()
# c.execute("insert into MESSAGES values(1488, 1337, 'hello')")
# conn.commit()

c.execute('select * from messages')
print(c.fetchone())
