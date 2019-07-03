# BasePerson, all Person objects should support these methods at a minimum
class BasePerson:
    def __init__(self):
        self._id = "BasePerson"

    def id(self):
        return self._id
