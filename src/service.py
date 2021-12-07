from entities.bnf import BNF, check_syntax
from entities.rule import Rule
from entities.sequence import Sequence
from entities.symbol import Symbol


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

    def load_bnf(self, id):
        bnfs = self._database.fetch_bnf(id)

        if len(bnfs) == 0:
            return

        bnf = bnfs[0]
        bnf_id = bnf[0]

        self.bnf = BNF(bnf_id)
        rules = self._database.fetch_all_rules(bnf_id)

        for rule_data in rules:
            rule_id = rule_data[0]
            rule = Rule(rule_data[2], [], rule_data[1], rule_data[0])
            self.bnf.rules.append(rule)

            sequences = self._database.fetch_all_sequences(rule_id)

            for sequence_data in sequences:
                sequence_id = sequence_data[0]
                sequence = Sequence([], sequence_data[1], sequence_data[0])
                rule.sequences.append(sequence)

                symbols = self._database.fetch_all_symbols(sequence_id)

                for symbol_data in symbols:
                    symbol = Symbol(symbol_data[3], symbol_data[2], symbol_data[1], symbol_data[0])
                    sequence.symbols.append(symbol)

    def get_list_of_bnfs(self):
        items = [item[0] for item in self._database.fetch_all_bnfs()]
        return items
