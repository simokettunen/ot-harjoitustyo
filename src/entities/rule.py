from entities.sequence import Sequence

class Rule():
    def __init__(self, symbol, sequences):
        self.symbol = symbol
        self.sequences = []
        self._init_sequences(sequences)

    def __str__(self):
        string = f'{self.symbol} ::= '

        for sequence in self.sequences:
            string += sequence.__str__()

        return string

    def _init_sequences(self, sequences):
        for sequence in sequences:
            symbol_list = sequence.split(' ')
            sequence_object = Sequence(symbol_list)
            self.sequences.append(sequence_object)
