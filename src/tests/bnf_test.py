import unittest
from bnf import check_syntax, BNF

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
        
    def test_sequence_consisting_of_single_terminal_is_handled_correctly(self):
        bnf = BNF()
        result = bnf._handle_sequence('"a"')
        self.assertListEqual(result, [{'label': 'a', 'type': 'terminal'}])
        
    def test_sequence_consisting_of_single_nonterminal_is_handled_correctly(self):
        bnf = BNF()
        result = bnf._handle_sequence('<a>')
        self.assertListEqual(result, [{'label': 'a', 'type': 'non-terminal'}])
        
    def test_sequence_consisting_of_two_terminals_is_handled_correctly(self):
        bnf = BNF()
        result = bnf._handle_sequence('"a" "b"')
        should_be = [
            {'label': 'a', 'type': 'terminal'},
            {'label': 'b', 'type': 'terminal'}
        ]
        self.assertListEqual(result, should_be)
        
    def test_rule_consisting_of_single_sequence_is_handled_correctly(self):
        bnf = BNF()
        result = bnf._handle_rule('<a>')
        self.assertListEqual(result, [[{'label': 'a', 'type': 'non-terminal'}]])
        
    def test_rule_consisting_of_two_sequences_is_handled_correctly(self):
        bnf = BNF()
        result = bnf._handle_rule('<a> | "b"')
        should_be = [
            [{'label': 'a', 'type': 'non-terminal'}],
            [{'label': 'b', 'type': 'terminal'}],
        ]
        self.assertListEqual(result, should_be)
        
    def test_bnf_model_consisting_of_single_rule_is_handled_correctly(self):
        bnf = BNF()
        bnf.create_from_string('a ::= <b> | "c"')
        should_be = [
            [
                [{'label': 'b', 'type': 'non-terminal'}],
                [{'label': 'c', 'type': 'terminal'}],
            ],
        ]
        self.assertListEqual(bnf.rules, should_be)
        
    def test_bnf_model_consisting_of_two_rules_is_handled_correctly(self):
        bnf = BNF()
        text = 'a ::= <b> | "c"'
        text += '\n'
        text += 'b ::= "e"'
        bnf.create_from_string(text)
        should_be = [
            [
                [{'label': 'b', 'type': 'non-terminal'}],
                [{'label': 'c', 'type': 'terminal'}],
            ],
            [
                [{'label': 'e', 'type': 'terminal'}],
            ],
        ]
        self.assertListEqual(bnf.rules, should_be)
        
        
        
        
        
        