import uuid
import SOLE


class BaseBuilding:
    default_attributes = {"height": None, "floors": [], "elevators": []}

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self._uuid = uuid.uuid1()
        self.attribute = BaseBuilding.default_attributes
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        running_height = 0
        for f in self.get("floors"):
            SOLE.log("manipulating floor {}".format(f.get("uuid")))
            f.set("elevation", running_height)
            running_height += f.get("height")
            f.set("elevation_top", running_height)
        self.set("height", running_height)

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        if name == "uuid":
            raise Exception("cannot manually set uuid for an object of this type")

        self.attribute[name] = value
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            if isinstance(self.attribute[name], list):
                return list(self.attribute[name])
            else:
                return self.attribute[name]
        else:
            return ""

    def uuid(self):
        """uuid() will return a unique identifier for the object"""
        return self._uuid

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("BaseBuilding->tick() for {}".format(self.uuid()))
        for f in self.get("floors"):
            f.tick()
        for e in self.get("elevators"):
            e.tick()
        # for e in elevator: e.tick()
        # for p in people: p.tick()
        # for f in floors: f.tick()
        return
