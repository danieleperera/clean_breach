import sqlite3


class DbHandler:

    def __init__(self, dbfile="database210.db"):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
        self.cur = self.connection.cursor()
        self.connection.execute('pragma journal_mode=MEMORY')
        self.connection.execute('pragma SYNCHRONOUS=1')
        self.connection.execute('pragma PAGE_SIZE=4096')
        self.connection.execute('pragma cache_size = 8192')
        self.connection.execute('pragma auto_vacuum=1')
        self.cur.execute('PRAGMA foreign_keys = ON')
        self.cache = []
        self.cache2 = []
        
#delete this after 

        self.get_id_username = 1

    def setup(self):
        statement = "CREATE TABLE IF NOT EXISTS usernametable (username text , id INTEGER NOT NULL PRIMARY KEY )"
        statement2 = "CREATE TABLE IF NOT EXISTS domaintable (domain text PRIMARY KEY, id_domain INTEGER NOT NULL, FOREIGN KEY(id_domain) REFERENCES usernametable(id))" #, FOREIGN KEY(id_domain) REFERENCES usernametable(id)
        self.cur.execute(statement)
        self.cur.execute(statement2)
        self.connection.commit()

    def add_item(self, email):
        username = email[:email.index("@")]
        #domain = email[email.index("@")+1:]
        #country = domain[domain.index("."):]
        self.check_domain_table(email)
        self.cache.append((username,)) # must keep the comma because it's a tuple

    def store_items(self):
        statement = "INSERT OR IGNORE INTO usernametable (username) VALUES (?)"
        statement_add_domain = "INSERT OR IGNORE INTO domaintable (domain, id_domain) VALUES (?, ?)"
        self.connection.executemany(statement, self.cache)
        #self.connection.commit()
        self.connection.executemany(statement_add_domain, self.cache2)
        self.connection.commit()
        self.cache = []
        self.cache2 = []

    def check_domain_table(self, email):
        username = email[:email.index("@")]
        domain = email[email.index("@")+1:]
        
        i = 1
        print(username +" id ====  "+str(self.get_id_username))
        self.get_id_username += i
        i +=1

        statement_check_domain = "SELECT EXISTS(SELECT 1 FROM domaintable WHERE domain=? LIMIT 1)"    
        self.cur.execute(statement_check_domain, (domain,))
        
        data=self.cur.fetchone()[0]
        if data==0:
            print('There is no domain named ' + domain + ' in the database')
            self.cache2.append((domain, int(self.get_id_username)-1))
        else:
            print('i have to point the username to the correct domain')

        
        """

                    print('There is no domain named' + domain + ' in the database')
            statement_add_domain = "INSERT INTO domaintable (domain, number) VALUES (?, ?)"
            self.cur.execute(statement_add_domain, (domain, int(self.get_id_username)))
            self.connection.commit()



        if self.cur.execute(statement_check_domain, (domain,)) == 0:
            print(domain + " added to database")
            #aggiungi e punta
            statement_add_domain = "INSERT INTO domaintable (domain, number) VALUES (?, ?)"
            self.cur.execute(statement_add_domain, (domain, self.id_of_username))
            self.connection.commit()
        else:
            #punta e basta
            statement_add_domain = "INSERT INTO domaintable (domain, number) VALUES (?, ?)"
            self.cur.execute(statement_add_domain, (domain, self.id_of_username))
            self.connection.commit()
            print("found "+ domain +" +++++++ adding pointer")


        

        [Finished in 37.1s]
        [Finished in 31.2s] without this part

        
        row = self.cur.execute(get_id_username)

        if row is not None:
            id_of_username = row
            print("okaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay")
            print(id_of_username)
        else:
            print("+++++++++++++++++++++++++ why +++++++++++++++++++++++++")
            # https://stackoverflow.com/questions/27718385/typeerror-nonetype-object-is-not-subscriptable
        """




        