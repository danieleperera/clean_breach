import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE breach (
            email text
            )""")
