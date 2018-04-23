import sqlite3

conn = sqlite3.connect('ServerStorage.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
# conn.execute('drop table OPEN_KEYS')
# conn.execute('drop table MESSAGES')  # message types: message; key-sharing
#
# c.execute('create table OPEN_KEYS (username text UNIQUE, openkey_x real, openkey_y real)')
# c.execute('create table MESSAGES (to_username text, from_username text, message text)')
#
#
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())
# c.execute("insert into OPEN_KEYS values('Anton', 1337, 1488)")
# conn.commit()

c.execute('select * from OPEN_KEYS')
print(c.fetchone())
