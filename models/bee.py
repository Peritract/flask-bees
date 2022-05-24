from random import choice

class Bee():

    _all = [(1, "Beeatrice", False), (2, "Beenard", False), (3, "Elizabeeth", False),
            (4, "Libbee", True), (5, 'Beelinda', True), (6, 'Beeata', True)]

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
    def create_bee(cls, id, name, queen):
        cls._all.append((id, name, queen))
        return Bee(id, name, queen)

    @classmethod
    def peaceful_transition(cls):
        # Get all the queens
        queens = list(filter(lambda x: x[2] == True, cls._all))

        # Count all the queens
        queen_count = len(queens)

        # If there's more than one queen
        if queen_count > 1:

            # Pick one
            regina = choice(queens)

            # Identify the failed claimants
            surplus = filter(lambda x: x[0] != regina[0], queens)

            # Destroy each one
            for q in surplus:
                Bee(*q).delete()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "queen": self.queen
        }

    def delete(self):
        print(self)
        Bee._all = list(filter(lambda x: x[0] != self.id, self._all))
