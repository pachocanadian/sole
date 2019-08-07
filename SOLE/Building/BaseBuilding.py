import SOLE
import pickle


class BaseBuilding:
    default_attributes = {"height": None, "floors": [], "elevators": [] }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = BaseBuilding.default_attributes
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseBuilding"))
        _elevation_of = dict()
        running_height = 0
        for f in self.get("floors"):
            floor_id = f.get("id")
            SOLE.log("manipulating floor {}".format( floor_id ), SOLE.LOG_INFO)
            f.set("elevation", running_height)
            _elevation_of[floor_id] = running_height
            running_height += f.get("height")
            f.set("elevation_top", running_height)
            f.set("building", self)
        self.set("height", running_height)
        self.set("_elevation_of", _elevation_of)

        elevators = self.get("elevators")
        for e in elevators:
            e.set("building", self)
        self.set("elevators", elevators)


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

    def elevation_of(self, object_id):
        eo = self.get("_elevation_of")
        if object_id in eo:
            return eo[object_id]
        else:
            return None

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseBuilding->tick()".format(self.get("id")), SOLE.LOG_INFO)
        for f in self.get("floors"):
            f.tick()
        for e in self.get("elevators"):
            e.tick()
        # for e in elevator: e.tick()
        # for p in people: p.tick()
        # for f in floors: f.tick()
        return
