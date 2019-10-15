import SOLE
import random


def sole_baseperson_random_name():
    possible_first_names = (
        "Mike",
        "Annika",
        "Bronwyn",
        "Katie",
        "Carol",
        "Jen",
        "Myrna",
        "Dane",
        "Jeanne",
        "Chrystal",
        "Brennon",
        "Greg",
        "Danielle",
        "Dawn",
        "Bruce",
        "Joyce",
        "Eve",
        "Ted",
        "Deidre",
        "Monica",
        "Toni",
        "Kevin",
        "Glenda",
        "Laura",
        "Tina",
        "Hollie",
        "Lhalic",
        "Andrea",
        "Sherry",
        "Jonathan",
        "Ashleigh",
        "Christian",
        "Rob",
        "Nathan",
        "Vanessa",
        "Angela",
        "Eva",
        "Bud",
        "Chloe",
    )
    return possible_first_names[random.randint(0, len(possible_first_names) - 1)]


class BasePerson:

    _default_attributes = {
        "height": 1.77,
        "location": None,  # a reference to the parent Elevator/Floor object
        "building": None,  # a reference to the parent building object
        "destination": None,  # a reference to the floor/elevator object that we are destined to
        "label": None,  # a human friendly identifier
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = {}
        for key in BasePerson._default_attributes:
            self.set(key, BasePerson._default_attributes[key])
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        if self.get("label") is None:
            self.set("label", sole_baseperson_random_name())
        self.set("id", SOLE.new_id("BasePerson"))

        if (
            self.get("location") is not None
            and self.get("destination_floor") is not None
        ):
            SOLE.log(
                "{} was created on {} with a destination of {}".format(
                    self.get("label"),
                    self.get("location").get("label"),
                    self.get("destination_floor").get("label"),
                ),
                SOLE.LOG_NOTICE,
            )

        SOLE.log("[{}] BasePerson->created".format(self.get("id")), SOLE.LOG_INFO)

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def __del__(self):
        """track destruction of object"""
        SOLE.log("[{}] BasePerson->destroyed".format(self.get("id")), SOLE.LOG_INFO)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""

        if name == "height":
            if not (value > 0):
                raise Exception("attribute height must be greater than zero")

        if name == "destination_floor":
            # if our destination_floor changes then indicate it to our carrying object if we're on a floor
            location = self.get("location")
            destination_floor = value
            if location is not None:
                if location.get("is_floor"):
                    if destination_floor is not None:
                        location.add_to_request_queue(location.get("id"))

        if name == "location":
            # if we are being added to a parent object then access its carrying attribute and add ourselves
            location = value
            destination_floor = self.get("destination_floor")
            if location is not None:
                location.get("carrying").append(self)

                if location.get("is_floor"):
                    if destination_floor is not None:
                        location.add_to_request_queue(destination_floor.get("id"))

                if self.get("building") is None:
                    self.set("building", value.get("building"))

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

        # Remove person from elevator's carrying list
        carrying = elevator.get("carrying")
        carrying.remove(self)

        # Check the destination for the person
        destination_floor = self.get("destination_floor")

        if floor == destination_floor:
            SOLE.log(
                "[{}] BasePerson reached destination={}".format(
                    self.get("id"), destination_floor.get("id")
                ),
                SOLE.LOG_INFO,
            )

            SOLE.log(
                "{} reached destination {}".format(
                    self.get("label"), destination_floor.get("label")
                ),
                SOLE.LOG_NOTICE,
            )

            self.set("location", None)
            del self
        else:
            # Set person's location attribute to the current floor.
            self.set("location", floor)

    def load(self, elevator, floor):
        """load() will add person to an elevator."""

        # Remove person from floors carrying list
        floor.get("carrying").remove(self)

        # Get the destination for the person
        destination_floor = self.get("destination_floor")

        # Set person's location attribute to the elevator
        self.set("location", elevator)
        elevator.add_to_request_queue(destination_floor.get("id"))

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BasePerson->tick()".format(self.get("id")), SOLE.LOG_INFO)
        carrying = self.get("carrying")
        if carrying is not None:
            self.set("elevation", self.get("carrying").get("elevation"))
