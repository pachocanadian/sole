import SOLE


class BasePerson:
    default_attributes = {"height": 1.77}

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = BasePerson.default_attributes
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BasePerson"))

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        if name == "height":
            if not (value > 0):
                raise Exception("attribute weight must be greater than zero")

        self.attribute[name] = value
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            return self.attribute[name]
        else:
            return None

    def unload(self, elevator, floor):
        """unload() to remove person from elevator."""

    #        Ask all elevators if they are carrying this person; if so then remove person.
    #        for elevator in SOLE.BaseBuilding.default_attributes["elevators"]:
    #            if self.get("id") in elevator.get("carrying"):

    def load(self, elevator, floor):
        """load() will add person to an elevator."""

        # Ask elevator if it is carrying this person; if not then add person.

    #        if self.get("id") not in elevator.get("carrying"):
    #            elevator.set(
    #                self.get("carrying"), self.get("carrying").append(self.get("id"))
    #            )
    #            return
    #
    #        raise Exception("Invalid elevator.")

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BasePerson->tick()".format(self.get("id")), SOLE.LOG_INFO)
        return
