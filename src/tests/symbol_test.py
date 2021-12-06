import unittest
import uuid
from entities.symbol import Symbol

class TestSymbol(unittest.TestCase):
    def setUp(self):
        self.id = str(uuid.uuid4())

    def test_str_returns_non_terminal_correctly(self):
        symbol = Symbol('a', 'non-terminal', self.id)
        self.assertEqual(symbol.__str__(), '<a>')

    def test_str_returns_terminal_correctly(self):
        symbol = Symbol('a', 'terminal', self.id)
        self.assertEqual(symbol.__str__(), '"a"')