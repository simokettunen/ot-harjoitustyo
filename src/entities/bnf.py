import re
import uuid
from entities.rule import Rule

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
    def __init__(self, bnf_id=None):
        self.rules = []

        if bnf_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = bnf_id

    def __str__(self):
        string = ''

        for rule in self.rules:
            if len(string) > 0:
                string += '\n'

            string += rule.__str__()

        return string

    def create_from_string(self, string):
        """Create a BNF model from the given input string"""

        # TODO: Consider adding syntax check here

        lines = string.split('\n')

        for line in lines:
            line = line.split(' ::= ')
            rule = Rule(line[0][1:-1], line[1].split(' | '), self.id)
            self.rules.append(rule)

    def check_unassigned_nonterminals(self):
        assigned_nonterminals = set()
        for rule in self.rules:
            assigned_nonterminals.add(rule.symbol)

        nonterminals = set()
        for rule in self.rules:
            for sequence in rule.sequences:
                for symbol in sequence.symbols:
                    if symbol.type == 'non-terminal':
                        nonterminals.add(symbol.label)

        if len(nonterminals - assigned_nonterminals) == 0:
            return True

        return False
