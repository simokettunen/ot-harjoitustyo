import warnings
from entities.bnf import BNF, check_syntax
from entities.rule import Rule
from entities.sequence import Sequence
from entities.symbol import Symbol

class Service():
    """Class, that acts as a BNF service,"""

    def __init__(self, database):
        """Constructor of the class.

        Args:
            database: instance of database class, that has a connection to database
        """

        self._database = database
        self.bnf = None

    def create_bnf(self, string=''):
        """Creates a BNF object from string and adds it to the service.

        Args:
            string: string that is used to create the model

        Returns:
            True, if string passes syntax check
            False, if string does not pass syntax check
        """

        is_correct_syntax = check_syntax(string)

        if is_correct_syntax:
            if self.bnf:
                self.bnf = BNF(self.bnf.id)
            else:
                self.bnf = BNF()
            self.bnf.create_from_string(string)

        return is_correct_syntax

    def save_bnf(self):
        """Saves BNF object stored in service to database."""

        if not self.bnf:
            return

        self.remove_bnf()
        self._database.add(self.bnf)

        for rule in self.bnf.rules:
            self._database.add(rule)

            for sequence in rule.sequences:
                self._database.add(sequence)

                for symbol in sequence.symbols:
                    self._database.add(symbol)

    def load_bnf(self, bnf_id):
        """Loads BNF model from database and stores it to service.

        Args:
            bnf_id: UUID of the BNF to be loaded
        """

        bnfs = self._database.fetch_single(bnf_id, 'bnf')

        if len(bnfs) == 0:
            warnings.warn(f'No bnf model found with id {bnf_id}')
            return

        bnf = bnfs[0]
        bnf_id = bnf[0]

        self.bnf = BNF(bnf_id)

        rules = self._database.fetch_all(bnf_id, 'rule')

        for rule_data in rules:
            rule_id = rule_data[0]
            rule = Rule(rule_data[2], [], rule_data[1], rule_data[0])
            self.bnf.rules.append(rule)

            sequences = self._database.fetch_all(rule_id, 'sequence')

            for sequence_data in sequences:
                sequence_id = sequence_data[0]
                sequence = Sequence([], sequence_data[1], sequence_data[0])
                rule.sequences.append(sequence)

                symbols = self._database.fetch_all(sequence_id, 'symbol')

                for symbol_data in symbols:
                    symbol = Symbol(symbol_data[3], symbol_data[2], symbol_data[1], symbol_data[0])
                    sequence.symbols.append(symbol)

    def remove_bnf(self):
        """Removes BNF model and all data related it from database."""

        for rule in self.bnf.rules:
            for sequence in rule.sequences:
                for symbol in sequence.symbols:
                    self._database.remove(symbol.id, 'symbol')

                self._database.remove(sequence.id, 'sequence')

            self._database.remove(rule.id, 'rule')

        self._database.remove(self.bnf.id, 'bnf')

    def get_list_of_bnfs(self):
        """Loads all BNF UUIDs from database.

        Returns:
            List of UUIDs of BNF models
        """

        items = [item[0] for item in self._database.fetch_all(None, 'bnf')]
        return items
