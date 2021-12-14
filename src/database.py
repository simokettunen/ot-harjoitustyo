import sqlite3

class Database:
    """ Class, that collects useful commands related to database.
    """

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
        """Adds a single BNF object into database

        Args:
            bnf_id: BNF's UUID
        """

        cur = self._con.cursor()
        cur.execute('INSERT INTO bnf VALUES (?)', (bnf_id,))
        self._con.commit()

    def add_rule(self, rule_id, bnf_id, symbol):
        """ Adds a single rule object into database

        Args:
            rule_id: rule's UUID
            bnf_id: UUID of BNF model in which the rule belongs to
            symbol: specifier of the rule, i.e. symbol on the left in the rule
        """

        cur = self._con.cursor()
        cur.execute('INSERT INTO rule VALUES (?, ?, ?)', (rule_id, bnf_id, symbol))
        self._con.commit()

    def add_sequence(self, sequence_id, rule_id):
        """ Adds a single sequence into database

        Args:
            sequence_id: sequence's UUID
            rule_id: UUID of rule in which the sequence belongs to
        """

        cur = self._con.cursor()
        cur.execute('INSERT INTO sequence VALUES (?, ?)', (sequence_id, rule_id))
        self._con.commit()

    def add_symbol(self, symbol_id, sequence_id, symbol_type, symbol_label):
        """ Adds a single symbol into database

        Args:
            symbol_id: symbol's UUID
            sequence_id: UUID of sequence in which the symbol belongs to
            symbol_type: type of the symbol (nonterminal or terminal)
            symbol_label: label of the symbol
        """

        cur = self._con.cursor()
        cur.execute('INSERT INTO symbol VALUES (?, ?, ?, ?)', (symbol_id, sequence_id, symbol_type, symbol_label))
        self._con.commit()

    def fetch_bnf(self, bnf_id):
        """ Fetches a single BNF from database

        Args:
            bnf_id: UUID of the BNF to be fetched

        Returns:
            list which contains BNF's UUID if it exists in the database
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM bnf WHERE id=?', (bnf_id,))
        return cur.fetchall()

    def fetch_all_bnfs(self):
        """ Fetches all BNFs from database

        Returns:
            list which contains all BNF UUID's from table bnf
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM bnf')
        return cur.fetchall()

    def fetch_rule(self, rule_id):
        """ Fetches a single rule from database

        Args:
            rule_id: UUID of the rule to be fetched

        Returns:
            list, which contains rule's UUID, UUID of BNF model in which the rule belongs to, and specifier of the rule, i.e. symbol on the left in the rule
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM rule WHERE id=?', (rule_id,))
        return cur.fetchall()

    def fetch_all_rules(self, bnf_id):
        """ Fetches all rules belonging to single BNF from database

        Args:
            bnf_id: UUID of the BNF whose rules are fetched from database

        Returns:
            list, which contains lists of rule's UUID, UUID of BNF model in which the rule belongs to, and specifier of the rule, i.e. symbol on the left in the rule
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM rule WHERE bnf=?', (bnf_id,))
        return cur.fetchall()

    def fetch_sequence(self, sequence_id):
        """ Fetches a single sequence from database

        Args:
            sequence_id: UUID of the sequence to be fetched

        Returns:
            list, which contains sequence's UUID and UUID of rule in which the sequence belongs to
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM sequence WHERE id=?', (sequence_id,))
        return cur.fetchall()

    def fetch_all_sequences(self, rule_id):
        """ Fetches all sequences belonging to single rule from database

        Args:
            rule_id: UUID of the rule whose rules are fetched from database

        Returns:
            list, which contains lists of sequence's UUID and UUID of rule in which the sequence belongs to
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM sequence WHERE rule=?', (rule_id,))
        return cur.fetchall()

    def fetch_symbol(self, symbol_id):
        """ Fetches a single symbol from database

        Args:
            symbol_id: UUID of the symbol to be fetched

        Returns:
            list, which contains UUID, UUID of the sequence, type and label
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM symbol WHERE id=?', (symbol_id,))
        return cur.fetchall()

    def fetch_all_symbols(self, sequence_id):
        """ Fetches all symbols belonging to single sequence from database

        Args:
            sequence_id: UUID of the sequence whose symbols are fetched from database

        Returns:
            list, which contains lists of UUID, UUID of the sequence, type and label
        """

        cur = self._con.cursor()
        cur.execute('SELECT * FROM symbol WHERE sequence=?', (sequence_id,))
        return cur.fetchall()

    def close_connection(self):
        """ Closes database connection
        """

        self._con.close()
