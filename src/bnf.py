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
