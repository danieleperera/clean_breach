import sqlite3


class DbHandler:
    
    def __init__(self, dbfile="database.db"):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
        self.cur = self.connection.cursor()
    
    def setup(self):
        statement = "CREATE TABLE IF NOT EXISTS breach (email text UNIQUE,username text,domain text,country text)"
        self.connection.execute(statement)
        self.connection.commit()
    
    def get_allrecords(self):
        statement = "SELECT * FROM breach"
        return [x for x in self.connection.execute(statement)]
    
    def add_items(self, emails):
        for email in emails:
            self._add_item(email)
        self.connection.commit()

    def _add_item(self, email):
        statement = "INSERT OR IGNORE INTO breach (email, username, domain, country) VALUES (?, ?, ?, ?)"
        #print(email)
        username = email[:email.index("@")]
        domain = email[email.index("@")+1:]
        country = domain[domain.index("."):]
        args = (email, username, domain, country)
        self.cur.execute(statement, args)


