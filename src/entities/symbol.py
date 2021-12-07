import uuid

class Symbol():
    def __init__(self, symbol_label, symbol_type, sequence_id, symbol_id=None):
        if symbol_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = symbol_id

        self.sequence_id = sequence_id
        self.label = symbol_label
        self.type = symbol_type

    def __str__(self):
        if self.type == 'non-terminal':
            return f'<{self.label}>'

        return f'"{self.label}"'
