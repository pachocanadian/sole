import uuid


class BaseBuilding:
    def __init__(self):
        self._id = uuid.uuid1()

    def getFloors(self):
        return self.floors

    def setFloors(self, f):
        self.floors = f

    def getElevators(self):
        return self.elevators

    def setElevators(self, e):
        self.elevators = e

    def id(self):
        return self._id
