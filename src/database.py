import sqlite3

class Database:
    def __init__(self, name='database.db'):
        self._con = sqlite3.connect(name)
        self._init_tables()

    def _init_tables(self):
        cur = self._con.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS bnf(
                id TEXT PRIMARY KEY
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS rule (
                id TEXT PRIMARY KEY,
                bnf INTEGER,
                symbol TEXT
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS sequence (
                id TEXT PRIMARY KEY,
                rule INTEGER
            );
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS symbol (
                id TEXT PRIMARY KEY,
                sequence INTEGER,
                type TEXT,
                label TEXT
             );
        ''')

    def add_bnf(self, bnf_id):
        cur = self._con.cursor()
        cur.execute('INSERT INTO bnf VALUES (?)', (bnf_id,))
        self._con.commit()

    def add_rule(self, rule_id, bnf_id, symbol):
        cur = self._con.cursor()
        cur.execute('INSERT INTO rule VALUES (?, ?, ?)', (rule_id, bnf_id, symbol))
        self._con.commit()

    def add_sequence(self, sequence_id, rule_id):
        cur = self._con.cursor()
        cur.execute('INSERT INTO sequence VALUES (?, ?)', (sequence_id, rule_id))
        self._con.commit()

    def add_symbol(self, symbol_id, sequence_id, symbol_type, symbol_label):
        cur = self._con.cursor()
        cur.execute('INSERT INTO symbol VALUES (?, ?, ?, ?)', (symbol_id, sequence_id, symbol_type, symbol_label))
        self._con.commit()

    def fetch_bnf(self, bnf_id):
        cur = self._con.cursor()
        cur.execute('SELECT * FROM bnf WHERE id=?', (bnf_id,))
        return cur.fetchall()

    def fetch_all_bnfs(self):
        cur = self._con.cursor()
        cur.execute('SELECT * FROM bnf')
        return cur.fetchall()

    def fetch_rule(self, rule_id):
        cur = self._con.cursor()
        cur.execute('SELECT * FROM rule WHERE id=?', (rule_id,))
        return cur.fetchall()

    def fetch_sequence(self, sequence_id):
        cur = self._con.cursor()
        cur.execute('SELECT * FROM sequence WHERE id=?', (sequence_id,))
        return cur.fetchall()

    def fetch_symbol(self, symbol_id):
        cur = self._con.cursor()
        cur.execute('SELECT * FROM symbol WHERE id=?', (symbol_id,))
        return cur.fetchall()

    def close_connection(self):
        self._con.close()
