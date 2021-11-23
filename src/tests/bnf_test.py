import unittest
from bnf import check_syntax

class TestBNF(unittest.TestCase):
    def test_correct_syntax_check_on_empty_input(self):
        text = ''
        result = check_syntax(text)
        self.assertTrue(check_syntax)