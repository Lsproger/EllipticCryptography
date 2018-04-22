import sqlite3

conn = sqlite3.connect('ServerStorage.db')
conn.execute('create table OPEN_KEYS (mac UNIQUE, openkey_x, openkey_y)')
conn.execute('create table MESSAGES (to_mac, from_mac, text, message_type)')  # message types: message; key-sharing
