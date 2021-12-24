import uuid
from entities.sequence import Sequence

class Rule():
    """Class presenting a rule in BNF model.

    Attributes:
        id: UUID of the rule
        bnf_id: UUID of BNF model in which rule belongs to
        symbol: specifier of the rule, i.e. symbol on the left in the rule
        sequences: list of sequences in the rule
    """

    def __init__(self, symbol, sequences, bnf_id, rule_id=None):
        """Constuctor of class Rule.

        Args:
            symbol: specifier of the rule, i.e. symbol on the left in the rule
            sequences: string that is used to create sequences of the rules
            bnf_id: UUID of BNF model in which rule belongs to
            rule_id: UUID of the rule, default is None
        """

        if rule_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = rule_id

        self.bnf_id = bnf_id
        self.symbol = symbol
        self.sequences = []
        self._init_sequences(sequences)

    def __str__(self):
        """Returns a string presentation of class Rule.

        Returns:
            String presentation of rule object
        """

        string = f'<{self.symbol}> ::= '

        flag_for_first = True
        for sequence in self.sequences:
            if flag_for_first:
                string += sequence.__str__()
                flag_for_first = False
            else:
                string += f' | {sequence.__str__()}'

        return string

    def _init_sequences(self, sequences):
        for sequence in sequences:
            symbol_list = sequence.split(' ')
            sequence_object = Sequence(symbol_list, self.id)
            self.sequences.append(sequence_object)
