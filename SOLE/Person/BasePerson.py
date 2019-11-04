import SOLE
import random
from SOLE.Settings.BaseSettings import BaseSettings


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

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.settings = BaseSettings(
            {
                "id": {
                    "type": "string",
                    "validation": "",
                    "default": "",
                    "comment": "A unique string identifying the object. Generally not human friendly.",
                },
                "height": {
                    "type": "float",
                    "validation": "gt_zero",
                    "default": 1.77,
                    "comment": "The height of the person.",
                },
                "location": {
                    "type": "reference",
                    "validation": "",
                    "default": None,
                    "comment": "A reference to the object the person is contained in, whether floor or elevator.",
                },
                "building": {
                    "type": "building",
                    "validation": "",
                    "default": None,
                    "comment": "A reference to the parent building.",
                },
                "destination": {
                    "type": "reference",
                    "validation": "",
                    "default": None,
                    "comment": "A reference to the floor/elevator that we are destined to.",
                },
                "label": {
                    "type": "string",
                    "validation": "",
                    "default": sole_baseperson_random_name(),
                    "comment": "A human friendly descriptor of the object.",
                },
            }
        )
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BasePerson"))

    def __str__(self):
        """allow print() to function in some intelligible way"""
        return "{}".format(self.settings)

    def __del__(self):
        """track destruction of object"""
        SOLE.log("[{}] BasePerson->destroyed".format(self.get("id")), SOLE.LOG_INFO)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        self.settings.set(name, value)
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        return self.settings.get(name)

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
        elevator.add_to_request_queue(destination_floor)

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BasePerson->tick()".format(self.get("id")), SOLE.LOG_INFO)
        carrying = self.get("carrying")
        if carrying is not None:
            self.set("elevation", self.get("carrying").get("elevation"))
