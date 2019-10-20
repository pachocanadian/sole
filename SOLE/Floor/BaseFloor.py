import SOLE
from SOLE.Settings.BaseSettings import BaseSettings


class BaseFloor:
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
                    "default": 3.00,
                    "comment": "The height of the floor",
                },
                "elevation": {
                    "type": "float",
                    "validation": "",
                    "default": 0.00,
                    "comment": "The distance of the bottom-most point of the object from the ground.",
                },
                "elevation_top": {
                    "type": "float",
                    "validation": "",
                    "default": 0.00,
                    "comment": "The distance of the top-most point of the object from the ground.",
                },
                "label": {
                    "type": "string",
                    "validation": "",
                    "default": "",
                    "comment": "A human friendly descriptor of the object.",
                },
                "carrying": {
                    "type": "list",
                    "validation": "",
                    "default": [],
                    "comment": "A list of the people contained within the floor object.",
                },
                "building": {
                    "type": "building",
                    "validation": "",
                    "default": None,
                    "comment": "A reference to the parent building object.",
                },
                "is_floor": {
                    "type": "boolean",
                    "validation": "",
                    "default": True,
                    "comment": "A boolean indicating whether we are a floor object or not.",
                },
            }
        )
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseFloor"))

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

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseFloor->tick()".format(self.get("id")), SOLE.LOG_INFO)
        for p in self.get("carrying"):
            p.tick()
        return

    def add_to_request_queue(self, floor_id):
        """add_to_request_queue() will pass on the request for floor_id to associated elevator for floor"""
        self.get("building").get("elevators")[0].add_to_request_queue(floor_id)
