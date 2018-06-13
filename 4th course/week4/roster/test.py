import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT title FROM Course WHERE id = 3')
val = cur.fetchone()
print(val)