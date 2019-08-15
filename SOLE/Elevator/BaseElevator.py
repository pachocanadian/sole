import SOLE

class BaseElevator:
    default_attributes = {
        "height": 2.44,
        "elevation": None,  # will calculate dynamically each tick
        "destination_floor": None,  # set dynamically during normal operation, in normal operation will return to startingFloor
        "velocity": 0,  # we start at rest. positive velocity is up, negative velocity is down
        "label": None,  # if the object has a friendly identifier
        "maximum_up_speed": 1,  # elevators generally can go up faster than down
        "maximum_down_speed": -1,  # elevators generally can go up faster than down
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
        if(name == "maximum_down_speed"):
            assert value < 0, "maximum_down_speed must be negative float"

        self.attribute[name] = value
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            return self.attribute[name]
        else:
            return None

    def change_velocity(self, velocity):
        """change_velocity(velocity) changes elevator velocity. Pass positive float for up, negative for down, and 0 for stop."""
        if(velocity == 0):
            self.set("velocity", velocity)
        elif(velocity > 0):
            self.set("velocity", self.get("maximum_up_speed"))
        elif(velocity < 0):
            self.set("velocity", self.get("maximum_down_speed"))
        else:
            assert(False, "unmatched velocity")

    def move(self):
        """move() moves the elevator by one unit of velocity."""
        self.set("elevation", (self.get("elevation") + self.get("velocity")))

    def unload(self):
        carrying = self.get("carrying")
        if(type(carrying) == list):
            for p in carrying:
                p.unload()

    def load(self):
        elevation = self.get("elevation")
        b = self.get("building")
        floor_id = b.at_elevation(elevation)
        carrying = b.ref_to(floor_id).get("carrying")
        if(type(carrying) == list):
            for p in carrying:
                p.load()

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseElevator->tick()".format(self.get("id")), SOLE.LOG_INFO)
        for p in self.get("carrying"):
            p.tick()

        b = self.get("building")
        elevation = self.get("elevation")
        destination_floor = self.get("destination_floor")
        destination_elevation = b.elevation_of(destination_floor)
        distance = (destination_elevation - elevation)
        velocity = self.get("velocity")

        if((velocity == 0) and (distance == 0)):
            self.unload()
            self.load()
            self.set("destination_floor", None)
        elif((distance > 0) and (distance < velocity)):
            self.set("elevation", destination_elevation)
            self.change_velocity(0)
            self.move()
        elif((distance < 0) and (distance > velocity)):
            self.set("elevation", destination_elevation)
            self.change_velocity(0)
            self.move()
        else:
            self.change_velocity(distance)
            self.move()



        SOLE.log(
            "[{}] destination_floor={}, destination_elevation={}, elevation={}, distance={}, velocity={}".format(
                self.get("id"), 
                destination_floor, 
                destination_elevation,
                elevation,
                distance,
                velocity
            ),
            SOLE.LOG_INFO
        )

        return
