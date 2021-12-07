from entities.bnf import BNF, check_syntax

class Service():
    def __init__(self, database):
        self._database = database
        self.bnf = None
        
    def create_bnf(self, string=''):
        is_correct_syntax = check_syntax(string)
        
        if is_correct_syntax:
            self.bnf = BNF()
            self.bnf.create_from_string(string)
       
        return is_correct_syntax

    def save_bnf(self):
        if self.bnf:
            self._database.add_bnf(self.bnf.id)

    def get_list_of_bnfs(self):
        items = [item[0] for item in self._database.fetch_all_bnfs()]
        return items
