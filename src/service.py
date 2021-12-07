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
        if not self.bnf:
            return

        self._database.add_bnf(self.bnf.id)

        for rule in self.bnf.rules:
            self._database.add_rule(
                rule.id,
                rule.bnf_id,
                rule.symbol,
            )

            for sequence in rule.sequences:
                self._database.add_sequence(
                    sequence.id,
                    sequence.rule_id,
                )

                for symbol in sequence.symbols:
                    self._database.add_symbol(
                        symbol.id,
                        symbol.sequence_id,
                        symbol.type,
                        symbol.label,
                    )

    def get_list_of_bnfs(self):
        items = [item[0] for item in self._database.fetch_all_bnfs()]
        return items
