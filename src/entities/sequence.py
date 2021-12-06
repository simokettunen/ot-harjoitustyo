import uuid
from entities.symbol import Symbol

class Sequence():
    def __init__(self, symbols, rule_id):
        self.id = str(uuid.uuid4())
        self.rule_id = rule_id
        self.symbols = []
        self._init_sequence(symbols)

    def __str__(self):
        string = ''

        for symbol in self.symbols:
            string += f'{symbol.__str__()} '

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
