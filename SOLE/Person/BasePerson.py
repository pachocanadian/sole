import uuid


class BasePerson:
    def __init__(self, name, weight):
        self._uuid = uuid.uuid1()
        self._name = name
        self._weight = weight

    def uuid(self):
        return self._uuid


    def getName(self):
        return self._name

    def setName(self, n):
        self._name = n


    def getWeight(self):
        return self._weight

    def setWeight(self, w):
        self._weight = w
