import unittest
import uuid
from entities.rule import Rule

class TestRule(unittest.TestCase):
    def setUp(self):
        self.id = str(uuid.uuid4())
        
    def test_str_returns_rule_consisting_of_single_sequence_correctly(self):
        rule = Rule('a', ['<b>'], self.id)
        
        self.assertEqual(rule.__str__(), '<a> ::= <b>')
        
    def test_str_returns_rule_consisting_of_two_sequences_correctly(self):
        rule = Rule('a', ['<b>', '"c"'], self.id)
        
        self.assertEqual(rule.__str__(), '<a> ::= <b> | "c"')
       
    def test_rule_consisting_of_single_sequence_is_constructed_correctly(self):
        # a ::= <b>
        rule = Rule('a', ['<b>'], self.id)
        
        self.assertEqual(len(rule.sequences), 1)
        self.assertEqual(rule.symbol, 'a')
        self.assertEqual(rule.sequences[0].symbols[0].label, 'b')
        self.assertEqual(rule.sequences[0].symbols[0].type, 'non-terminal')
        self.assertEqual(rule.sequences[0].rule_id, rule.id)
        
    def test_rule_consisting_of_two_sequences_is_handled_correctly(self):
        # a ::= <b> | "c"
        rule = Rule('a', ['<b>', '"c"'], self.id)
        
        self.assertEqual(len(rule.sequences), 2)
        self.assertEqual(rule.symbol, 'a')
        self.assertEqual(rule.sequences[0].symbols[0].label, 'b')
        self.assertEqual(rule.sequences[0].symbols[0].type, 'non-terminal')
        self.assertEqual(rule.sequences[1].rule_id, rule.id)
        self.assertEqual(rule.sequences[1].symbols[0].label, 'c')
        self.assertEqual(rule.sequences[1].symbols[0].type, 'terminal')
        self.assertEqual(rule.sequences[1].rule_id, rule.id)