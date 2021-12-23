import re
import uuid
from entities.rule import Rule

def check_syntax(text):
    """Checks if the given collection of BNF rules has correct syntax.

    Args:
        text: string that is checked

    Returns:
        True, if string passes syntax check
    """

    lines = text.split('\n')

    prog = re.compile(r'^<[a-z]+> ::= ((<[a-z]+>|"[a-z]+")( (<[a-z]+>|"[a-z]+"))*)( \| (<[a-z]+>|"[a-z]+")( (<[a-z]+>|"[a-z]+"))*)*$')

    for line in lines:

        if line == '':
            continue

        if not prog.match(line):
            return False

    return True

class BNF():
    """  Class presenting a BNF model

    Attributes:
        rules: list of rules in the BNF model
        id: UUID of the model
    """

    def __init__(self, bnf_id=None):
        """ Constructor of class BNF

        Args:
            bnf_id: UUID of BNF, default is None
        """

        self.rules = []

        if bnf_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = bnf_id

    def __str__(self):
        """ Returns a string presentation of class BNF

        Returns:
            string presentation of BNF object
        """

        string = ''

        for rule in self.rules:
            if len(string) > 0:
                string += '\n'

            string += rule.__str__()

        return string

    def create_from_string(self, string):
        """ Creates a BNF model from the given input string

        Args:
            string: string that is used in creating a BNF object
        """

        # TODO: Consider adding syntax check here

        if string == '':
            return

        lines = string.split('\n')

        for line in lines:
            if line == '':
                continue
        
            line = line.split(' ::= ')
            rule = Rule(line[0][1:-1], line[1].split(' | '), self.id)
            self.rules.append(rule)

    def check_unassigned_nonterminals(self):
        """ Checks if BNF model has unassigned nonterminals

        Returns:
            True, if none unassigned nonterminals appears in the BNF model
        """

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

