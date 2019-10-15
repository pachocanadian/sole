import SOLE
from SOLE.Settings.BaseSettings import BaseSettings


class BaseElevator:
    _default_attributes = {
        "height": 2.44,
        "elevation": None,  # will calculate dynamically each tick
        "destination_floor": None,  # set dynamically during normal operation, in normal operation will return to startingFloor
        "velocity": 0,  # we start at rest. positive velocity is up, negative velocity is down
        "label": None,  # if the object has a friendly identifier
        "maximum_up_speed": 1,  # elevators generally can go up faster than down
        "maximum_down_speed": -1,  # elevators generally can go up faster than down
        "carrying": None,  # a list of Person objects presently within the elevator
        "building": None,  # a reference to the parent building
        "floor_requests": None,  # a list of Floor ID's in sequential order
        "status": "waiting",  # a string outlining what activity we are currently performing
        "status_percent": 1,  # a float from 0..1 indicating percentage completion of the status
        "unloading_time_needed": 5,  # float in real-world seconds
        "loading_time_needed": 5,  # float in real-world seconds
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.settings = BaseSettings(
            {
                "height": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 2.44,
                    "comment": "The height of the elevator itself.",
                },
                "elevation": {
                    "type": "float",
                    "validation": "",
                    "default": None,
                    "comment": "The elevation of the top-most point of the elevator.",
                },
                "destination_floor": {
                    "type": "floor",
                    "validation": "",
                    "default": None,
                    "comment": "The current destination floor that we are moving towards. Set to None when not in motion.",
                },
                "velocity": {
                    "type": "float",
                    "validation": "",
                    "default": 0,
                    "comment": "Positive velocity means upwards, negative means downward, 0 is at rest",
                },
                "label": {
                    "type": "string",
                    "validation": "",
                    "default": None,
                    "comment": "A friendly identifier for the elevator",
                },
                "maximum_up_speed": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 1,
                    "comment": "A maximum upward velocity for the elevator, must be >0",
                },
                "maximum_down_speed": {
                    "type": "float",
                    "validation": "lt_zero",
                    "default": 1,
                    "comment": "A maximum downward velocity for the elevator, must be <0",
                },
                "carrying": {
                    "type": "list",
                    "validation": "",
                    "default": [],
                    "comment": "A list of Person objects presently within the elevator",
                },
                "building": {
                    "type": "reference",
                    "validation": "",
                    "default": None,
                    "comment": "A reference to the current building object the elevator is contained within.",
                },
                "floor_requests": {
                    "type": "list",
                    "validation": "",
                    "default": [],
                    "comment": "A list of floor requests in sequential order.",
                },
                "status": {
                    "type": "string",
                    "validation": "",
                    "default": "waiting",
                    "comment": "The current status of the elevator.",
                },
                "status_percent": {
                    "type": "float",
                    "validation": "is_percent",
                    "default": 1.00,
                    "comment": "A float inside [0,1] indicating percentage completion of status.",
                },
                "unloading_time_needed": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 5.00,
                    "comment": "Real world seconds that it takes to unload the elevator.",
                },
                "loading_time_needed": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 5.00,
                    "comment": "Real world seconds that it takes to load the elevator.",
                },
            }
        )
        self.attribute = {}
        for key in BaseElevator._default_attributes:
            self.set(key, BaseElevator._default_attributes[key])
        self.set("floor_requests", [])
        self.set("carrying", [])
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
        self.set(
            "elevation",
            (
                self.get("elevation")
                + (self.get("velocity") / SOLE.tick_ratio_to_real_time)
            ),
        )

    def unload(self):
        """unload() iterates through the elevators carrying attribute and dumps out passengers"""
        SOLE.log("[{}] BaseElevator->unload()".format(self.get("id")), SOLE.LOG_INFO)
        elevation = self.get("elevation")
        b = self.get("building")
        floor_id = b.at_elevation(elevation)
        floor = b.ref_to(floor_id)
        carrying = self.get("carrying")
        if type(carrying) == list:
            for p in carrying:
                if p.get("destination_floor") == floor:
                    SOLE.log(
                        "Unloaded {} from the elevator at the {}".format(
                            p.get("label"), floor.get("label")
                        )
                    )
                    p.unload(self, floor)

    def load(self):
        """load() iterates through the floors carrying attribute and loads up passenges"""
        SOLE.log("[{}] BaseElevator->load()".format(self.get("id")), SOLE.LOG_INFO)
        elevation = self.get("elevation")
        b = self.get("building")
        floor_id = b.at_elevation(elevation)
        floor = b.ref_to(floor_id)
        carrying = floor.get("carrying")
        if type(carrying) == list:
            for p in carrying:
                SOLE.log(
                    "Loaded {} into the elevator from the {}".format(
                        p.get("label"), floor.get("label")
                    )
                )
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
                    building = self.get("building")
                    destination_floor = building.ref_to(floor_id)
                    self.set("destination_floor", destination_floor)
                    SOLE.log(
                        "{} moving to {}".format(
                            self.get("label"), destination_floor.get("label")
                        ),
                        SOLE.LOG_NOTICE,
                    )

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseElevator->tick()".format(self.get("id")), SOLE.LOG_INFO)
        SOLE.log(
            "[{}] BaseElevator->tick() elevation={:.2f} status={} status_percent={:.0%}".format(
                self.get("id"),
                self.get("elevation"),
                self.get("status"),
                self.get("status_percent"),
            ),
            SOLE.LOG_DEBUG,
        )

        # iterate through each of the people we are carrying and let them tick()
        for p in self.get("carrying"):
            p.tick()

        valid_statuses = ("waiting", "unloading", "loading", "moving")

        b = self.get("building")
        elevation = self.get("elevation")
        destination_floor = self.get("destination_floor")
        status = self.get("status")
        status_percent = self.get("status_percent")

        # from unloading state, we can either continue unloading or start loading
        if status == "unloading":
            self.unload()
            if status_percent >= 1.00:
                self.set("status", "loading")
                self.set("status_percent", 0)
                return

            self.set("status", "unloading")
            self.set(
                "status_percent",
                status_percent
                + 1
                / (self.get("unloading_time_needed") * SOLE.tick_ratio_to_real_time),
            )
            return

        # from loading state, we can either continue loading or start waiting
        if status == "loading":
            self.load()
            if status_percent >= 1.00:
                self.set("status", "waiting")
                self.set("status_percent", 0)
                return

            self.set("status", "loading")
            self.set(
                "status_percent",
                status_percent
                + 1 / (self.get("loading_time_needed") * SOLE.tick_ratio_to_real_time),
            )
            return

        # from waiting state, we can either continue waiting or start moving
        if status == "waiting":
            if destination_floor is None:
                # check if there is any new destinations to move to
                self.queue()
                destination_floor = self.get("destination_floor")

            if destination_floor is None:
                # continue to wait if there is still no destination floor
                self.set(status, "waiting")
                self.set(status_percent, 1.00)
                return

            if destination_floor is not None:
                # there is a destination floor so start moving next tick
                self.set("status", "moving")
                self.set("status_percent", 0.00)
                return

        if status == "moving":
            destination_elevation = destination_floor.get("elevation")
            distance = destination_elevation - elevation
            velocity = self.get("velocity")

            SOLE.log(
                "BaseElevator (moving) my_elevation={:.2f} destination_floor={} destination_elevation={:.2f} distance={:.2f} velocity={:.2f}".format(
                    self.get("elevation"),
                    self.get("destination_floor").get("id"),
                    destination_elevation,
                    distance,
                    velocity,
                ),
                SOLE.LOG_DEBUG,
            )

            # if we've arrived then stop and unload next tick
            if distance == 0:
                SOLE.log(
                    "{} has arrived at {}".format(
                        self.get("label"), destination_floor.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination_floor", None)
                self.change_velocity(0)
                self.set("status", "unloading")
                self.set("status_percent", 0)
                return

            if (distance > 0) and (
                distance < (velocity / SOLE.tick_ratio_to_real_time)
            ):
                SOLE.log(
                    "{} has arrived at {}".format(
                        self.get("label"), destination_floor.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination_floor", None)
                self.set("elevation", destination_elevation)
                self.change_velocity(0)
                self.set("status", "unloading")
                self.set("status_percent", 0)
                return

            elif (distance < 0) and (
                distance > (velocity / SOLE.tick_ratio_to_real_time)
            ):
                SOLE.log(
                    "{} has arrived at {}".format(
                        self.get("label"), destination_floor.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination_floor", None)
                self.set("elevation", destination_elevation)
                self.change_velocity(0)
                self.set("status", "unloading")
                self.set("status_percent", 0)
                return

            else:

                self.change_velocity(distance)
                velocity = self.get("velocity")
                self.move()
                self.set("status", "moving")
                self.set(
                    "status_percent", distance
                )  # TOFIX: NEED TO KEEP TRACK OF RELATIVE DISTANCE TRAVELLED FOR % TO WORK
                return

        return
