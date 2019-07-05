import uuid


class BaseBuilding:
    def __init__(self):
        self._uuid = uuid.uuid1()

        # Add a building to total when a class inherits this class.
        self._totalBuildings += 1
    
    def returnTotalBuildings():
        return self._totalBuildings

    def destroyBuilding():
        # Destroy an instance of abuilding class. Add extra code as needed.
        self._totalBuildings -= 1

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
