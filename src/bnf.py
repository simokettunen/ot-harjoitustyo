import re

def check_syntax(text):
    lines = text.split('\n')
    
    prog = re.compile(r'<[a-z]> ::= ((<[a-z]>|\"\s\")( (<[a-z]>|\"\s\"))*)(\| (<[a-z]>|\"\s\")( (<[a-z]>|\"\s\"))*)*')

    for line in lines:
    
        if line == '':
            continue
    
        if not prog.match(line):
            return False
        
    return True

class BNF():
    def __init__(self):
        self.lines = []