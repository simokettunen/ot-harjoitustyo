import unittest
import uuid
from database import Database
from entities.symbol import Symbol
from entities.sequence import Sequence
from entities.rule import Rule
from entities.bnf import BNF

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.id = str(uuid.uuid4())
        self.database = Database('temp.db')
    
    def test_adding_symbol_to_database_works_correctly(self):
        symbol = Symbol('a', 'non-terminal', self.id)
        self.database.add_symbol(
            symbol.id,
            symbol.sequence_id,
            symbol.type,
            symbol.label
        )
        
        result = self.database.fetch_symbol(symbol.id)[0]
        
        self.assertTupleEqual(result, (symbol.id, symbol.sequence_id, symbol.type, symbol.label))

    def test_adding_sequence_to_database_works_correctly(self):
        sequence = Sequence(['<a>'], self.id)
        self.database.add_sequence(sequence.id, sequence.rule_id)
        result = self.database.fetch_sequence(sequence.id)[0]
        
        self.assertTupleEqual(result, (sequence.id, sequence.rule_id))
        
    def test_adding_rule_to_database_works_correctly(self):
        rule = Rule('a', ['<b>'], self.id)
        self.database.add_rule(rule.id, rule.bnf_id, rule.symbol)
        result = self.database.fetch_rule(rule.id)[0]
        
        self.assertTupleEqual(result, (rule.id, rule.bnf_id, rule.symbol))

    def test_adding_bnf_to_database_work_correctly(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b>')
        self.database.add_bnf(bnf.id)
        result = self.database.fetch_bnf(bnf.id)[0]
        
        self.assertTupleEqual(result, (bnf.id,))