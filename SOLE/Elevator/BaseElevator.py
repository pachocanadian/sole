import SOLE
from SOLE.Settings.BaseSettings import BaseSettings


class BaseElevator:
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
                    "default": 0.00,
                    "comment": "The elevation of the top-most point of the elevator.",
                },
                "destination": {
                    "type": "floor",
                    "validation": "",
                    "default": None,
                    "comment": "The current destination floor that we are moving towards. Set to None when not in motion.",
                },
                "velocity": {
                    "type": "float",
                    "validation": "",
                    "default": 0.00,
                    "comment": "Positive velocity means upwards, negative means downward, 0 is at rest",
                },
                "label": {
                    "type": "string",
                    "validation": "",
                    "default": "",
                    "comment": "A friendly identifier for the elevator",
                },
                "maximum_up_speed": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 1.00,
                    "comment": "A maximum upward velocity for the elevator, must be >0",
                },
                "maximum_down_speed": {
                    "type": "float",
                    "validation": "lt_zero",
                    "default": -1.00,
                    "comment": "A maximum downward velocity for the elevator, must be <0",
                },
                "carrying": {
                    "type": "list",
                    "validation": "",
                    "default": [],
                    "comment": "A list of Person objects presently within the elevator",
                },
                "building": {
                    "type": "building",
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
                    "default": "idle",
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
                "id": {
                    "type": "string",
                    "validation": "",
                    "default": "",
                    "comment": "A unique string identifying the object. Generally not human friendly.",
                },
            }
        )
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseElevator"))

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        self.settings.set(name, value)
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        return self.settings.get(name)

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
                if p.get("destination") == floor:
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

    def add_to_request_queue(self, floor):
        """add_to_request_queue(floor_id) will add floor_id to the list of floors to travel to"""
        SOLE.log(
            "[{}] BaseElevator->add_to_request_queue({})".format(self.get("id"), floor),
            SOLE.LOG_INFO,
        )

        self.get("floor_requests").append(floor)

    def queue(self):
        """queue() will iterate through the queue of floor_requests if there is no current desination_floor"""
        SOLE.log("[{}] BaseElevator->queue()".format(self.get("id")), SOLE.LOG_INFO)
        if self.get("destination") is None:
            if type(self.get("floor_requests")) == list:
                if len(self.get("floor_requests")) > 0:
                    floor_requests = self.get("floor_requests")
                    destination = floor_requests.pop(0)
                    if destination is None:
                        pass
                    else:
                        self.set("destination", destination)
                        SOLE.log(
                            "{} moving to {}".format(
                                self.get("label"), destination.get("label")
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

        valid_statuses = (
            "idle",
            "unloading",
            "loading",
            "moving",
            "doors_opening",
            "doors_open",
            "doors_closing"
        )

        b = self.get("building")
        elevation = self.get("elevation")
        destination = self.get("destination")
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
                min(
                    status_percent
                    + 1
                    / (
                        self.get("unloading_time_needed") * SOLE.tick_ratio_to_real_time
                    ),
                    1,
                ),
            )
            return

        # from loading state, we can either continue loading or start idle
        if status == "loading":
            self.load()
            if status_percent >= 1.00:
                self.set("status", "idle")
                self.set("status_percent", 0)
                return

            self.set("status", "loading")
            self.set(
                "status_percent",
                min(
                    status_percent
                    + 1
                    / (self.get("loading_time_needed") * SOLE.tick_ratio_to_real_time),
                    1,
                ),
            )
            return

        # from idle state, we can either continue idle or start moving
        if status == "idle":
            if destination is None:
                # check if there is any new destinations to move to
                self.queue()
                destination = self.get("destination")

            if destination is None:
                # continue to wait if there is still no destination floor
                self.set(status, "idle")
                self.set(status_percent, 1.00)
                return

            if destination is not None:
                # there is a destination floor so start moving next tick
                self.set("status", "moving")
                self.set("status_percent", 0.00)
                return

        if status == "moving":
            destination_elevation = destination.get("elevation")
            distance = destination_elevation - elevation
            velocity = self.get("velocity")

            SOLE.log(
                "BaseElevator (moving) my_elevation={:.2f} destination={} destination_elevation={:.2f} distance={:.2f} velocity={:.2f}".format(
                    self.get("elevation"),
                    self.get("destination").get("id"),
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
                        self.get("label"), destination.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination", None)
                self.change_velocity(0)
                self.set("status", "unloading")
                self.set("status_percent", 0)
                return

            if (distance > 0) and (
                distance < (velocity / SOLE.tick_ratio_to_real_time)
            ):
                SOLE.log(
                    "{} has arrived at {}".format(
                        self.get("label"), destination.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination", None)
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
                        self.get("label"), destination.get("label")
                    ),
                    SOLE.LOG_NOTICE,
                )
                self.set("destination", None)
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
                    "status_percent", 1.00
                )  # TOFIX: NEED TO KEEP TRACK OF RELATIVE DISTANCE TRAVELLED FOR % TO WORK
                return

        return
