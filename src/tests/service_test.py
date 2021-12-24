import os
import unittest
import uuid
from database import Database
from service import Service
from entities.bnf import BNF

class TestDatabase(unittest.TestCase):
    def setUp(self):
        if os.path.isfile('temp.db'):
            os.remove('temp.db')
            
        self.id = str(uuid.uuid4())
        
        self.database = Database('temp.db')
        self.service = Service(self.database)
        
    def test_creating_bnf_works_with_correct_syntax(self):
        self.service.create_bnf('<a> ::= <b>')
        self.assertEqual(self.service.bnf.__str__(), '<a> ::= <b>')

    def test_creating_bnf_works_with_incorrect_syntax(self):
        self.service.create_bnf('<a> := <b>')
        self.assertIsNone(self.service.bnf)

    def test_saving_bnf_works(self):
        bnf = BNF()
        text = '<a> ::= <b>'
        self.service.create_bnf(text)
        self.service.save_bnf()
        result_bnf = self.database.fetch_single(self.service.bnf.id, 'bnf')[0]
        result_rule = self.database.fetch_all(self.service.bnf.id, 'rule')[0]
        result_sequence = self.database.fetch_all(result_rule[0], 'sequence')[0]
        result_symbol = self.database.fetch_all(result_sequence[0], 'symbol')[0]
        
        self.assertTupleEqual(result_bnf, (self.service.bnf.id,))
        self.assertTupleEqual(result_rule, (
            self.service.bnf.rules[0].id,
            self.service.bnf.rules[0].bnf_id,
            'a',
        ))
        self.assertTupleEqual(result_sequence, (
            self.service.bnf.rules[0].sequences[0].id,
            self.service.bnf.rules[0].sequences[0].rule_id,
        ))
        self.assertTupleEqual(result_symbol, (
            self.service.bnf.rules[0].sequences[0].symbols[0].id,
            self.service.bnf.rules[0].sequences[0].symbols[0].sequence_id,
            'non-terminal',
            'b',
        ))
        
    def test_loading_bnf_works(self):
        text = '<a> ::= <b>'
        self.service.create_bnf(text)
        self.service.save_bnf()
        bnf_id = self.service.bnf.id
        self.service.bnf = None
        self.service.load_bnf(bnf_id)
        
        self.assertEqual(self.service.bnf.__str__(), '<a> ::= <b>')
        
    def test_removing_bnf_works(self):
        text = '<a> ::= <b>'
        self.service.create_bnf(text)
        self.service.save_bnf()
        self.service.remove_bnf()
        result_bnf = self.database.fetch_all(self.service.bnf.id, 'bnf')
        result_rule = self.database.fetch_all(self.service.bnf.id, 'rule')
        result_sequence = self.database.fetch_all(self.service.bnf.rules[0].id, 'sequence')
        result_symbol = self.database.fetch_all(self.service.bnf.rules[0].sequences[0].id, 'symbol')
        self.assertListEqual(result_bnf, [])
        self.assertListEqual(result_rule, [])
        self.assertListEqual(result_sequence, [])
        self.assertListEqual(result_symbol, [])
        