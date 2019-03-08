import sqlite3


class DbHandler:
    
    def __init__(self, dbfile="database.db"):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
    
    def setup(self):
        statement = "CREATE TABLE IF NOT EXISTS breach (email text UNIQUE,username text,domain text,country text)"
        self.connection.execute(statement)
        self.connection.commit()
    
    def get_allrecords(self):
        statement = "SELECT * FROM breach"
        return [x for x in self.connection.execute(statement)]
    
    def add_item(self, email, username, domain, country):
        statement = "INSERT OR IGNORE INTO breach (email, username, domain, country) VALUES (?, ?, ?, ?)"
        args = (email, username, domain, country)
        self.connection.execute(statement, args)
        self.connection.commit()


