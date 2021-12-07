import unittest
import uuid
from entities.sequence import Sequence

class TestSequence(unittest.TestCase):
    def setUp(self):
        self.id = str(uuid.uuid4())
        
    def test_str_returns_sequence_consisting_of_single_symbol_correctly(self):
        sequence = Sequence(['"a"'], self.id)
        
        self.assertEqual(sequence.__str__(), '"a"')
        
    def test_str_returns_sequence_consisting_of_two_symbols_correctly(self):
        sequence = Sequence(['"a"', '<b>'], self.id)
        
        self.assertEqual(sequence.__str__(), '"a" <b>')
    
    def test_sequence_consisting_of_single_terminal_is_constructed_correctly(self):
        sequence = Sequence(['"a"'], self.id)
        
        self.assertEqual(len(sequence.symbols), 1)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)
        
    def test_sequence_consisting_of_single_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['<a>'], self.id)
        
        self.assertEqual(len(sequence.symbols), 1)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)

    def test_sequence_consisting_of_two_sequential_terminals_is_constructed_correctly(self):
        sequence = Sequence(['"a"', '"b"'], self.id)
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'terminal')
        self.assertEqual(sequence.symbols[1].sequence_id, sequence.id)
        
    def test_sequence_consisting_of_two_sequential_non_terminals_is_constructed_correctly(self):
        sequence = Sequence(['<a>', '<b>'], self.id)
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'non-terminal')
        self.assertEqual(sequence.symbols[1].sequence_id, sequence.id)
        
    def test_sequence_consisting_of_sequential_terminal_and_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['"a"', '<b>'], self.id)
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'non-terminal')
        self.assertEqual(sequence.symbols[1].sequence_id, sequence.id)
        
    def test_sequence_consisting_of_sequential_non_terminal_and_non_terminal_is_constructed_correctly(self):
        sequence = Sequence(['<a>', '"b"'], self.id)
        
        self.assertEqual(len(sequence.symbols), 2)
        self.assertEqual(sequence.symbols[0].label, 'a')
        self.assertEqual(sequence.symbols[0].type, 'non-terminal')
        self.assertEqual(sequence.symbols[0].sequence_id, sequence.id)
        self.assertEqual(sequence.symbols[1].label, 'b')
        self.assertEqual(sequence.symbols[1].type, 'terminal')
        self.assertEqual(sequence.symbols[1].sequence_id, sequence.id)