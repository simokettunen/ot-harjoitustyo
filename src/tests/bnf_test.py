import unittest
from entities.bnf import check_syntax, BNF

class TestBNF(unittest.TestCase):
    def test_correct_syntax_check_on_empty_input(self):
        text = ''
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_single_terminal(self):
        text = '<a> ::= "b"'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_single_nonterminal(self):
        text = '<a> ::= <b>'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_sequential_nonterminal_and_terminal(self):
        text = '<a> ::= "b" <c>'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_sequential_terminal_and_nonterminal(self):
        text = '<a> ::= <b> "c"'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_two_sequential_terminals(self):
        text = '<a> ::= "b" "c"'
        result = check_syntax(text)
        self.assertTrue(result)
 
    def test_correct_syntax_check_on_two_sequential_nonterminals(self):
        text = '<a> ::= <b> <c>'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_two_sequential_sequences(self):
        text = '<a> ::= <b> | <c>'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_three_sequential_sequences(self):
        text = '<a> ::= <b> | "c" <d> | "e"'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_correct_syntax_check_on_two_rules(self):
        text = '<a> ::= <b> | "c" <d> | "e"'
        text += '\n'
        text += '<f> ::= <g> | "h" <i> | "i"'
        result = check_syntax(text)
        self.assertTrue(result)
        
    def test_str_returns_bnf_model_consisting_of_single_rule_correctly(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b> | "c"')
        
        self.assertEqual(bnf.__str__(), 'a ::= <b> | "c"')
        
    def test_str_returns_bnf_model_consisting_of_two_rules_correctly(self):
        bnf = BNF()
        text = 'a ::= <b> | "c"'
        text += '\n'
        text += 'b ::= "e"'
        bnf.create_from_string(text)
        
        self.assertEqual(bnf.__str__(), 'a ::= <b> | "c"\nb ::= "e"')
        
    def test_bnf_model_consisting_of_single_rule_is_handled_correctly(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b> | "c"')
        
        self.assertEqual(len(bnf.rules), 1)
        self.assertEqual(bnf.rules[0].symbol, 'a')
        self.assertEqual(bnf.rules[0].sequences[0].symbols[0].label, 'b')
        self.assertEqual(bnf.rules[0].sequences[0].symbols[0].type, 'non-terminal')
        self.assertEqual(bnf.rules[0].sequences[1].symbols[0].label, 'c')
        self.assertEqual(bnf.rules[0].sequences[1].symbols[0].type, 'terminal')
        self.assertEqual(bnf.rules[0].bnf_id, bnf.id)
        
    def test_bnf_model_consisting_of_two_rules_is_handled_correctly(self):
        bnf = BNF()
        text = 'a ::= <b> | "c"'
        text += '\n'
        text += 'b ::= "e"'
        bnf.create_from_string(text)
        
        self.assertEqual(len(bnf.rules), 2)
        self.assertEqual(bnf.rules[0].symbol, 'a')
        self.assertEqual(bnf.rules[0].sequences[0].symbols[0].label, 'b')
        self.assertEqual(bnf.rules[0].sequences[0].symbols[0].type, 'non-terminal')
        self.assertEqual(bnf.rules[0].sequences[1].symbols[0].label, 'c')
        self.assertEqual(bnf.rules[0].sequences[1].symbols[0].type, 'terminal')
        self.assertEqual(bnf.rules[0].bnf_id, bnf.id)
        self.assertEqual(bnf.rules[1].symbol, 'b')
        self.assertEqual(bnf.rules[1].sequences[0].symbols[0].label, 'e')
        self.assertEqual(bnf.rules[1].sequences[0].symbols[0].type, 'terminal')
        self.assertEqual(bnf.rules[1].bnf_id, bnf.id)
