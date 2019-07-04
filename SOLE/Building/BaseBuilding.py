import uuid


class BaseBuilding:
    def __init__(self):
        self._uuid = uuid.uuid1()

    def getFloors(self):
        return self.floors

    def setFloors(self, f):
        self.floors = f

    def getElevators(self):
        return self.elevators

    def setElevators(self, e):
        self.elevators = e

    def uuid(self):
        return self._uuid
