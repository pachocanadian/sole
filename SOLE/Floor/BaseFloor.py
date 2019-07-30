import uuid
import json
import SOLE


class BaseFloor:
    default_attributes = {
        "height": 3,
        "elevation": None,
        "elevation_top": None,
        "label": None,  # if the object has a friendly identifier
        "carrying": [],  # a list of Person objects presently within the elevator
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self._uuid = uuid.uuid1()
        self.attribute = {}
        for key in BaseFloor.default_attributes:
            self.set(key, BaseFloor.default_attributes[key])
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

        if name == "label":
            if not (str(value).strip()):
                raise Exception("attribute label must not be empty")

        self.attribute[name] = json.dumps(value)
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            return json.loads(self.attribute[name])
        else:
            return ""

    def uuid(self):
        """uuid() will return a unique identifier for the object"""
        return self._uuid

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("BaseFloor->tick() for {}".format(self.uuid()))
        for p in self.get("carrying"):
            p.tick()
        return
