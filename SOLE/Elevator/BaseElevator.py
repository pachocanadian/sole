import SOLE


class BaseElevator:
    _default_attributes = {
        "height": 2.44,
        "elevation": None,  # will calculate dynamically each tick
        "destination_floor": None,  # set dynamically during normal operation, in normal operation will return to startingFloor
        "velocity": 0,  # we start at rest. positive velocity is up, negative velocity is down
        "label": None,  # if the object has a friendly identifier
        "maximum_up_speed": 1,  # elevators generally can go up faster than down
        "maximum_down_speed": -1,  # elevators generally can go up faster than down
        "carrying": [],  # a list of Person objects presently within the elevator
        "floor_requests": [],  # a list of Floor ID's in sequential order
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = {}
        for key in BaseElevator._default_attributes:
            self.set(key, BaseElevator._default_attributes[key])
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseElevator"))

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        if name == "maximum_down_speed":
            assert value < 0, "maximum_down_speed must be negative float"

        if name == "maximum_up_speed":
            assert value > 0, "maximum_up_speed must be positive float"

        if name == "velocity":
            if value > 0:
                assert value <= self.get(
                    "maximum_up_speed"
                ), "upward velocity must be <= maximum_up_speed"
            if value < 0:
                assert value >= self.get(
                    "maximum_down_speed"
                ), "downward velocity must be >= maximum_down_speed"

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
        if velocity == 0:
            self.set("velocity", velocity)
        elif velocity > 0:
            self.set("velocity", self.get("maximum_up_speed"))
        elif velocity < 0:
            self.set("velocity", self.get("maximum_down_speed"))
        else:
            assert (False, "unmatched velocity")

    def move(self):
        """move() moves the elevator by one unit of velocity."""
        self.set("elevation", (self.get("elevation") + self.get("velocity")))

    def unload(self):
        elevation = self.get("elevation")
        b = self.get("building")
        floor_id = b.at_elevation(elevation)
        floor = b.ref_to(floor_id)
        carrying = self.get("carrying")
        if type(carrying) == list:
            for p in carrying:
                p.unload(self, floor)

    def load(self):
        elevation = self.get("elevation")
        b = self.get("building")
        floor_id = b.at_elevation(elevation)
        floor = b.ref_to(floor_id)
        carrying = floor.get("carrying")
        if type(carrying) == list:
            for p in carrying:
                p.load(self, floor)

    def add_to_request_queue(self, floor_id):
        """add_to_request_queue(floor_id) will add floor_id to the list of floors to travel to"""
        SOLE.log(
            "[{}] BaseElevator->add_to_request_queue({})".format(
                self.get("id"), floor_id
            ),
            SOLE.LOG_INFO,
        )

        self.get("floor_requests").append(floor_id)

    def queue(self):
        """queue() will iterate through the queue of floor_requests if there is no current desination_floor"""
        SOLE.log("[{}] BaseElevator->queue()".format(self.get("id")), SOLE.LOG_INFO)
        if self.get("destination_floor") is None:
            if type(self.get("floor_requests")) == list:
                if len(self.get("floor_requests")) > 0:
                    floor_id = self.get("floor_requests").pop(0)
                    self.set("destination_floor", floor_id)

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseElevator->tick()".format(self.get("id")), SOLE.LOG_INFO)
        for p in self.get("carrying"):
            p.tick()

        b = self.get("building")
        elevation = self.get("elevation")
        destination_floor = self.get("destination_floor")

        if destination_floor is None:
            self.queue()
            destination_floor = self.get("destination_floor")

        if destination_floor is None:
            return

        destination_elevation = b.elevation_of(destination_floor)
        distance = destination_elevation - elevation
        velocity = self.get("velocity")

        if (velocity == 0) and (distance == 0):
            self.unload()
            self.load()
            self.set("destination_floor", None)
            self.queue()
        elif (distance > 0) and (distance < velocity):
            self.set("elevation", destination_elevation)
            self.change_velocity(0)
            self.move()
        elif (distance < 0) and (distance > velocity):
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
                velocity,
            ),
            SOLE.LOG_INFO,
        )

        return
