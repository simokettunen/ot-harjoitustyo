import re

def check_syntax(text):
    """Check if the given collection of BNF rules has correct syntax."""
    lines = text.split('\n')

    prog = re.compile(r'^<[a-z]+> ::= ((<[a-z]+>|"[a-z]+")( (<[a-z]+>|"[a-z]+"))*)( \| (<[a-z]+>|"[a-z]+")( (<[a-z]+>|"[a-z]+"))*)*$')

    for line in lines:

        if line == '':
            continue

        if not prog.match(line):
            return False

    return True

class BNF():
    def __init__(self):
        self.lines = []

    def _handle_sequence(self, symbols):
        """Create a single sequence from the given input string"""
        symbols = symbols.split(' ')

        symbol_list = []

        for symbol in symbols:
            if symbol[0] == '"':
                symbol_type = 'terminal'
            elif symbol[0] == '<':
                symbol_type = 'non-terminal'

            symbol_list.append({
                'type': symbol_type,
                'label': symbol[1:-1],
            })

        return symbol_list

    def _handle_rule(self, sequences):
        """Create a single BNF rule from the given input string"""
        sequences = sequences.split(' | ')
        rule = []

        for sequence in sequences:
            rule.append(self._handle_sequence(sequence))

        return rule

    def create_from_string(self, input):
        """Create a BNF model from the given input string"""
        rules = input.split('\n')

        for rule in rules:
            rule = rule.split(' ::= ')
            rule_symbol = rule[0]
            line = self._handle_rule(rule[1])
            self.lines.append(line)
