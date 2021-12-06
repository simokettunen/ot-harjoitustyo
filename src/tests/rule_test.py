import unittest
from entities.rule import Rule

class TestRule(unittest.TestCase):
    def test_rule_consisting_of_single_sequence_is_constructed_correctly(self):
        # a ::= <b>
        rule = Rule('a', ['<b>'])
        
        self.assertEqual(len(rule.sequences), 1)
        self.assertEqual(rule.symbol, 'a')
        self.assertEqual(rule.sequences[0].symbols[0].label, 'b')
        self.assertEqual(rule.sequences[0].symbols[0].type, 'non-terminal')
        
    def test_rule_consisting_of_two_sequences_is_handled_correctly(self):
        # a ::= <b> | "c"
        rule = Rule('a', ['<b>', '"c"'])
        
        self.assertEqual(len(rule.sequences), 2)
        self.assertEqual(rule.symbol, 'a')
        self.assertEqual(rule.sequences[0].symbols[0].label, 'b')
        self.assertEqual(rule.sequences[0].symbols[0].type, 'non-terminal')
        self.assertEqual(rule.sequences[1].symbols[0].label, 'c')
        self.assertEqual(rule.sequences[1].symbols[0].type, 'terminal')