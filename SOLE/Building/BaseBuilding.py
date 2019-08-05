import SOLE
import pickle


class BaseBuilding:
    default_attributes = {"height": None, "floors": [], "elevators": []}

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = BaseBuilding.default_attributes
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseBuilding"))
        running_height = 0
        for f in self.get("floors"):
            SOLE.log("manipulating floor {}".format(f.get("id")))
            f.set("elevation", running_height)
            running_height += f.get("height")
            f.set("elevation_top", running_height)
        self.set("height", running_height)

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        self.attribute[name] = pickle.dumps(value)
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            return pickle.loads(self.attribute[name])
        else:
            return ""

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseBuilding->tick()".format(self.get("id")))
        for f in self.get("floors"):
            f.tick()
        for e in self.get("elevators"):
            e.tick()
        # for e in elevator: e.tick()
        # for p in people: p.tick()
        # for f in floors: f.tick()
        return
