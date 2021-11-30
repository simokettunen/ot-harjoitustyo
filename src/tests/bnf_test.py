import unittest
from bnf import check_syntax

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