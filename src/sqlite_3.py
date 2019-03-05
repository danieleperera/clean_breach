import sqlite3

conn = sqlite3.connect('breach.db')

c = conn.cursor()

c.execute("""CREATE TABLE breach (
            email text,
            domain text
            )""")

conn.commit()
conn.close()