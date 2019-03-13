import sqlite3


class DbHandler:
   
    def __init__(self, dbfile="database_using_pragma13.db"):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
        self.cur = self.connection.cursor()
        self.connection.execute('pragma journal_mode=MEMORY')
        self.connection.execute('pragma SYNCHRONOUS=1')
        self.connection.execute('pragma PAGE_SIZE=4096')
        self.connection.execute('pragma cache_size = 8192')
        self.connection.execute('pragma auto_vacuum=1') 
        self.cache = []
   
    def setup(self):
        statement = "CREATE TABLE IF NOT EXISTS breach (username text PRIMARY KEY,domain text,country text)"
        self.connection.execute(statement)
        self.connection.commit()
   
    def get_allrecords(self):
        statement = "SELECT * FROM breach"
        return [x for x in self.connection.execute(statement)]
   
    def add_item(self, email):
        username = email[:email.index("@")]
        domain = email[email.index("@"):]
        country = domain[domain.index("."):]
        self.cache.append((username, domain, country))

    def store_items(self):
        statement = "INSERT OR IGNORE INTO breach (username, domain, country) VALUES (?, ?, ?)"
        self.connection.executemany(statement, self.cache)
        self.connection.commit()
        self.cache = []