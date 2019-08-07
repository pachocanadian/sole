import SOLE
import pickle

class BaseElevator:
    default_attributes = {
        "height": 2.44,
        "elevation": None,  # will calculate dynamically each tick
        "destination_floor": None,  # set dynamically during normal operation, in normal operation will return to startingFloor
        "velocity": 0,  # we start at rest. positive velocity is up, negative velocity is down
        "label": None,  # if the object has a friendly identifier
        "maximum_up_speed": 1,  # elevators generally can go up faster than down
        "maximum_down_speed": 1,  # elevators generally can go up faster than down
        "carrying": [],  # a list of Person objects presently within the elevator
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = {}
        for key in BaseElevator.default_attributes:
            self.set(key, BaseElevator.default_attributes[key])
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseElevator"))

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

    def changeMovement(self, value):
        """ Modify velocity. Pass positive float for up, negative for down, and 0 for no velocity."""
        self.set("velocity", value)

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseElevator->tick()".format(self.get("id")), SOLE.LOG_INFO)
        for p in self.get("carrying"):
            p.tick()

        b = self.get("building")
        destination_floor = self.get("destination_floor")

        SOLE.log(
            "[{}] current destination floor is {} ({}) with elevator at {}".format(
                self.get("id"), 
                destination_floor, 
                b.elevation_of(destination_floor),
                self.get("elevation")
            ),
            SOLE.LOG_INFO
        )

        return
