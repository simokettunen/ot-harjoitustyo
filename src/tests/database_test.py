import os
import unittest
import uuid
from database import Database
from entities.bnf import BNF
from entities.rule import Rule
from entities.sequence import Sequence
from entities.symbol import Symbol

class TestDatabase(unittest.TestCase):
    def setUp(self):
        if os.path.isfile('temp.db'):
            os.remove('temp.db')
            
        self.id = str(uuid.uuid4())
        self.database = Database('temp.db')

    def test_adding_bnf_to_database_works(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b>')
        self.database.add(bnf)
        result = self.database.fetch_single(bnf.id, 'bnf')[0]
        
        self.assertTupleEqual(result, (bnf.id,))
        
    def test_adding_rule_to_database_works(self):
        rule = Rule('a', ['<b>'], self.id)
        self.database.add(rule)
        result = self.database.fetch_single(rule.id, 'rule')[0]
        
        self.assertTupleEqual(result, (rule.id, rule.bnf_id, rule.symbol))

    def test_adding_sequence_to_database_works(self):
        sequence = Sequence(['<a>'], self.id)
        self.database.add(sequence)
        result = self.database.fetch_single(sequence.id, 'sequence')[0]
        
        self.assertTupleEqual(result, (sequence.id, sequence.rule_id))

    def test_adding_symbol_to_database_works(self):
        symbol = Symbol('a', 'non-terminal', self.id)
        self.database.add(symbol)
        result = self.database.fetch_single(symbol.id, 'symbol')[0]
        
        self.assertTupleEqual(result, (symbol.id, symbol.sequence_id, symbol.type, symbol.label))
        
    def test_fetching_all_bnfs_from_database_works(self):
        bnf1 = BNF()
        bnf2 = BNF()
        bnf1.create_from_string('a ::= <b>')
        bnf2.create_from_string('b ::= <c>')
        self.database.add(bnf1)
        self.database.add(bnf2)
        result = self.database.fetch_all(None, 'bnf')
        
        self.assertTrue((bnf1.id,) in result)
        self.assertTrue((bnf2.id,) in result)
        
    def test_fetching_all_rules_from_database_works(self):
        rule1 = Rule('a', ['<b>'], self.id)
        rule2 = Rule('b', ['"c"'], self.id)
        self.database.add(rule1)
        self.database.add(rule2)
        result = self.database.fetch_all(self.id, 'rule')
        
        self.assertTrue((rule1.id, rule1.bnf_id, rule1.symbol) in result)
        self.assertTrue((rule2.id, rule2.bnf_id, rule2.symbol) in result)
        
    def test_fetching_all_sequences_from_database_works(self):
        sequence1 = Sequence(['<a>'], self.id)
        sequence2 = Sequence(['<b>'], self.id)
        self.database.add(sequence1)
        self.database.add(sequence2)
        result = self.database.fetch_all(self.id, 'sequence')
        
        self.assertTrue((sequence1.id, sequence1.rule_id) in result)
        self.assertTrue((sequence2.id, sequence2.rule_id) in result)
        
    def test_fetching_all_symbols_from_database_works(self):
        symbol1 = Symbol('a', 'non-terminal', self.id)
        symbol2 = Symbol('b', 'terminal', self.id)
        self.database.add(symbol1)
        self.database.add(symbol2)
        result = self.database.fetch_all(self.id, 'symbol')
        
        self.assertTrue((symbol1.id, symbol1.sequence_id, symbol1.type, symbol1.label) in result)
        self.assertTrue((symbol2.id, symbol2.sequence_id, symbol2.type, symbol2.label) in result)
        
    def test_removing_bnf_from_database_works(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b>')
        self.database.add(bnf)
        self.database.remove(bnf.id, 'bnf')
        result = self.database.fetch_all(bnf.id, 'bnf')
        
        self.assertListEqual(result, [])
        
    def test_removing_rule_from_database_works(self):
        rule = Rule('a', ['<b>'], self.id)
        self.database.add(rule)
        self.database.remove(rule.id, 'rule')
        result = self.database.fetch_single(rule.id, 'rule')
        
        self.assertListEqual(result, [])
              
    def test_removing_sequence_from_database_works(self):
        sequence = Sequence(['<a>'], self.id)
        self.database.add(sequence)
        self.database.remove(sequence.id, 'sequence')
        result = self.database.fetch_single(sequence.id, 'sequence')
        
        self.assertListEqual(result, [])
               
    def test_removing_symbol_from_database_works(self):
        symbol = Symbol('a', 'non-terminal', self.id)
        self.database.add(symbol)
        self.database.remove(symbol.id, 'symbol')
        result = self.database.fetch_single(symbol.id, 'symbol')
        
        self.assertListEqual(result, [])