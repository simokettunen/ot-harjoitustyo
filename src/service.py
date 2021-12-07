class Service():
    def __init__(self, database):
        self._database = database

    def add_bnf(self, bnf):
        self._database.add_bnf(bnf.id)

    def get_list_of_bnfs(self):
        items = [item[0] for item in self._database.fetch_all_bnfs()]
        return items
