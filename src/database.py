import sqlite3
import warnings

from entities.bnf import BNF
from entities.rule import Rule
from entities.sequence import Sequence
from entities.symbol import Symbol

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
        
    def add(self, item):
        """Adds an BNF model, rule, sequence or symbol in database.
        
        Args:
            item: item to be added, must be instance of any following classes: BNF, Rule, Sequence,
                Symbol
                
        """
        
        cur = self._con.cursor()
        
        if isinstance(item, BNF):
            cur.execute('INSERT INTO bnf VALUES (?)', (item.id,))
            
        elif isinstance(item, Rule):
            cur.execute('INSERT INTO rule VALUES (?, ?, ?)', (item.id, item.bnf_id, item.symbol))
            
        elif isinstance(item, Sequence):
            cur.execute('INSERT INTO sequence VALUES (?, ?)', (item.id, item.rule_id))
            
        elif isinstance(item, Symbol):
            cur.execute('INSERT INTO symbol VALUES (?, ?, ?, ?)', (item.id, item.sequence_id, item.type, item.label))
            
        else:
            warning.warn(f'Unknown item type: {item}')
            return
            
        self._con.commit()
        
    def fetch_single(self, id, item_type):
        """Fetches a single BNF model, rule, sequence or symbol from database.
        
        Args:
            id: UUID of the item
            item_type (string): type of item, (bnf, rule, sequence, symbol)
            
        Returns:
            Returns data from database according to type of item:
                For bnf: list which contains BNF's UUID if it exists in the database
                For rule: list, which contains rule's UUID, UUID of BNF model in which the rule belongs to, and specifier of the rule, i.e. symbol on the left in the rule
                For sequence: list, which contains sequence's UUID and UUID of rule in which the sequence belongs to
                For symbol: list, which contains UUID, UUID of the sequence, type and label
        
        """
        
        cur = self._con.cursor()
        
        if item_type == 'bnf':
            cur.execute('SELECT * FROM bnf WHERE id=?', (id,))
            
        elif item_type == 'rule':
            cur.execute('SELECT * FROM rule WHERE id=?', (id,))
            
        elif item_type == 'sequence':
            cur.execute('SELECT * FROM sequence WHERE id=?', (id,))
            
        elif item_type == 'symbol':
            cur.execute('SELECT * FROM symbol WHERE id=?', (id,))
            
        else:
            warning.warn(f'Unknown item type: {item_type}')
            return
            
        return cur.fetchall()
        
    def fetch_all(self, id, item_type):
        """Fetches a single BNF model, rule, sequence or symbol from database.
        
        Args:
            id: UUID of the parent of the item, or none if item is bnf
            item_type (string): type of item, (bnf, rule, sequence, symbol)
            
        Returns:
            Returns data from database according to type of item:
                For bnf: list which contains all BNF UUID's from table bnf
                For rule: list, which contains lists of rule's UUID, UUID of BNF model in which the rule belongs to, and specifier of the rule, i.e. symbol on the left in the rule
                For sequence: list, which contains lists of sequence's UUID and UUID of rule in which the sequence belongs to
                For symbol: list, which contains lists of UUID, UUID of the sequence, type and label
        
        """
        
        cur = self._con.cursor()
        
        if item_type == 'bnf':
            cur.execute('SELECT * FROM bnf')
            
        elif item_type == 'rule':
            cur.execute('SELECT * FROM rule WHERE bnf=?', (id,))
            
        elif item_type == 'sequence':
            cur.execute('SELECT * FROM sequence WHERE rule=?', (id,))
            
        elif item_type == 'symbol':
            cur.execute('SELECT * FROM symbol WHERE sequence=?', (id,))
            
        else:
            warning.warn(f'Unknown item type: {item_type}')
            return
            
        return cur.fetchall()
        
    def remove(self, id, item_type):
        """Removes a single BNF model, rule, sequence or symbol from database.
        
        Args:
            id: UUID of the parent of the item, or none if item is bnf
            item_type (string): type of item, (bnf, rule, sequence, symbol)
            
        """
        
        cur = self._con.cursor()
        
        if item_type == 'bnf':
            cur.execute('DELETE FROM bnf WHERE ID=?', (id,))
            
        elif item_type == 'rule':
            cur.execute('DELETE FROM rule WHERE ID=?', (id,))
            
        elif item_type == 'sequence':
            cur.execute('DELETE FROM sequence WHERE ID=?', (id,))
            
        elif item_type == 'symbol':
            cur.execute('DELETE FROM symbol WHERE ID=?', (id,))
            
        else:
            warning.warn(f'Unknown item type: {item_type}')
            return
            
        self._con.commit()

    def close_connection(self):
        """ Closes database connection
        """

        self._con.close()
