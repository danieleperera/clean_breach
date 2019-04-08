import sqlite3


class DbHandler:

    def __init__(self, dbfile="database.db"):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
        self.cur = self.connection.cursor()
        self.connection.execute('pragma journal_mode=MEMORY')
        self.connection.execute('pragma SYNCHRONOUS=1')
        self.connection.execute('pragma PAGE_SIZE=4096')
        self.connection.execute('pragma cache_size = 8192')
        self.connection.execute('pragma auto_vacuum=1')
        self.cur.execute('PRAGMA foreign_keys = ON')
        self.username_cache = []
        self.domain_cache = []
        
        # Local cache of domaintable. We need it for speed improvement of inserting into domaintable
        self.database_domain_cache = {}
        # This one indicates next domain_id in insert
        self.next_domain_id = 1
 
    def setup(self):
        statement = """
            CREATE TABLE IF NOT EXISTS
                domaintable
                (
                    domain_id INTEGER PRIMARY KEY,
                    domain TEXT UNIQUE
                )
        """
        self.cur.execute(statement)
        
        statement = """
            CREATE TABLE IF NOT EXISTS
                usernametable
                (
                    id INTEGER PRIMARY KEY,
                    username text NOT NULL,
                    domain_id INTEGER,
                    FOREIGN KEY(domain_id) REFERENCES domaintable(domain_id)
                )
        """
        self.cur.execute(statement)

        self.connection.commit()

        # Load domains from database into local cache, domain name is a key and domain_id is a value
        for domain_id, domain in self.connection.execute('SELECT * FROM domaintable').fetchall():
            self.database_domain_cache[domain] = domain_id
            if domain_id >= self.next_domain_id:
                self.next_domain_id = domain_id + 1
 
    def add_item(self, email):
        username = email[:email.index("@")]
        domain = email[email.index("@")+1:]
        #country = domain[domain.index("."):]
       
        # We have to check if domain exists in local cache first, we loaded all existing domains at script start (code above)
        # If it does not exist, create cache entry and prepare for database insert
        if domain not in self.database_domain_cache:
            # Add new domain into database domain cache with next id
            self.database_domain_cache[domain] = self.next_domain_id
            # Add to sql cache, to be inserted in store_items()
            # We want to insert domain name with given id we prepared for it
            self.domain_cache.append((self.next_domain_id, domain))
            # Increment next id
            self.next_domain_id += 1
    
        # Additionally to username we want to insert domain id here as well
        self.username_cache.append((username, self.database_domain_cache[domain]))
 
    def store_items(self):
        statement = "INSERT OR IGNORE INTO domaintable (domain_id, domain) VALUES (?,?)"
        self.connection.executemany(statement, self.domain_cache)
        
        statement = "INSERT OR IGNORE INTO usernametable (username, domain_id) VALUES (?,?)"
        self.connection.executemany(statement, self.username_cache)
       
        self.connection.commit()
        self.username_cache = []
        self.domain_name = []