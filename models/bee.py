class Bee():

    _all = [(1, "Beeatrice", False), (2, "Beenard", False), (3, "Elizabeeth", False),
            (4, "Libbee", True)]

    def __init__(self, id, name, queen=False):
        self.id = id
        self.name = name
        self.queen = queen

    def __repr__(self):
        return f"A bee called {self.name}"

    @classmethod
    def get_all_as_dicts(cls):
        return [Bee(*b).to_dict() for b in  cls._all]

    @classmethod
    def get_one_by_id(cls, id):
        match = list(filter(lambda x: x[0] == id, cls._all))
        if len(match) == 1:
            return Bee(*match[0])
        else:
            raise Exception("No matching bee found.")

    @classmethod
    def create_bee(cls, id, name, location):
        cls._all.append((id, name, location))
        return Bee(id, name, location)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "queen": self.queen
        }

    def delete(self):
        Bee._all = list(filter(lambda x: x[0] != self.id, self._all))
