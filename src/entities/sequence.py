import uuid
from entities.symbol import Symbol

class Sequence():
    """  Class presenting a sequence in a rule

    Attributes:
        id: UUID of the sequence
        rule_id: UUID of rule in which the sequence belongs to
        sequences: list of symbols in the rule
    """

    def __init__(self, symbols, rule_id, sequence_id=None):
        """ Constuctor of class Rule

        Args:
            symbols: string that is used to create symbols of the sequence
            rule_id: UUID of rule in which sequence belongs to
            sequence_id: UUID of the sequence, default is None
        """

        if sequence_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = sequence_id

        self.rule_id = rule_id
        self.symbols = []
        self._init_sequence(symbols)

    def __str__(self):
        """ Returns a string presentation of class Sequence

        Returns:
            string presentation of sequence object
        """

        string = ''

        for symbol in self.symbols:
            if len(string) == 0:
                string += f'{symbol.__str__()}'
            else:
                string += f' {symbol.__str__()}'

        return string

    def _init_sequence(self, symbols):
        for symbol in symbols:
            if symbol[0] == '"':
                symbol_type = 'terminal'
            elif symbol[0] == '<':
                symbol_type = 'non-terminal'

            symbol_label = symbol[1:-1]

            symbol_object = Symbol(symbol_label, symbol_type, self.id)
            self.symbols.append(symbol_object)
