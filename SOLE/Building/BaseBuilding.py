import uuid
import SOLE


class BaseBuilding:
    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self._uuid = uuid.uuid1()
        self.attribute = dict()
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])

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
            return self.attribute[name]
        else:
            return ""

    def uuid(self):
        """uuid() will return a unique identifier for the object"""
        return self._uuid

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("BaseBuilding->tick() for {}".format(self.uuid()))
        # for e in elevator: e.tick()
        # for p in people: p.tick()
        # for f in floors: f.tick()
        return
