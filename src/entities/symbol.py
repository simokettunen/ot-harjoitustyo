import uuid

class Symbol():
    """Class presenting a sequence in a rule.

    Attributes:
        id: UUID of the symbol
        sequence_id: UUID of sequence in which the symbol belongs to
        label: label of the symbol
        type: type of the symbol
    """

    def __init__(self, symbol_label, symbol_type, sequence_id, symbol_id=None):
        """Constuctor of class Symbol.

        Args:
            symbol_label: label of the symbol
            symbol_type: type of the symbol
            sequence_id: UUID of sequence in which the symbol belongs to
            symbol_id: UUID of symbol, default None
        """

        if symbol_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = symbol_id

        self.sequence_id = sequence_id
        self.label = symbol_label
        self.type = symbol_type

    def __str__(self):
        """Returns a string presentation of class Symbol.

        Returns:
            String presentation of symbol object
        """
        if self.type == 'non-terminal':
            return f'<{self.label}>'

        return f'"{self.label}"'
