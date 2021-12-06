import unittest
from entities.sequence import Sequence

class TestSequence(unittest.TestCase):
    def test_sequence_consisting_of_single_terminal_is_constructed_correctly(self):
        sequence = Sequence(['"a"'])
        
        self.assertEqual(len(sequence.symbols), 1)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        
    def test_sequence_consisting_of_single_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['<a>'])
        
        self.assertEqual(len(sequence.symbols), 1)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')

    def test_sequence_consisting_of_two_sequential_terminals_is_constructed_correctly(self):
        sequence = Sequence(['"a"', '"b"'])
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'terminal')
        
    def test_sequence_consisting_of_two_sequential_non_terminals_is_constructed_correctly(self):
        sequence = Sequence(['<a>', '<b>'])
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'non-terminal')
        
    def test_sequence_consisting_of_sequential_terminal_and_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['"a"', '<b>'])
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'non-terminal')
        
    def test_sequence_consisting_of_sequential_non_terminal_and_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['<a>', '"b"'])
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'terminal')