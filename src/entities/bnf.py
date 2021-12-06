import re
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
    def __init__(self):
        self.rules = []

    def __str__(self):
        string = ''

        for rule in self.rules:
            string += rule.__str__()
            string += '\n'

        return string

    def create_from_string(self, string):
        """Create a BNF model from the given input string"""
        lines = string.split('\n')

        for line in lines:
            line = line.split(' ::= ')
            rule = Rule(line[0], line[1].split(' | '))
            self.rules.append(rule)
