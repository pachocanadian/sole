# BaseBuilding, all Buildings should support these methods at a minimum
class BaseBuilding:
    def __init__(self, f, e):
        self.floors = f
        self.elevators = e
        self._id = "BaseBuilding"

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
