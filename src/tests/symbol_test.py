import unittest
from entities.symbol import Symbol

class TestSymbol(unittest.TestCase):
    def test_str_returns_non_terminal_correctly(self):
        symbol = Symbol('a', 'non-terminal')
        self.assertEqual(symbol.__str__(), '<a>')

    def test_str_returns_terminal_correctly(self):
        symbol = Symbol('a', 'terminal')
        self.assertEqual(symbol.__str__(), '"a"')