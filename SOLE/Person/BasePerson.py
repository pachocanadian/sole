import SOLE


class BasePerson:
    _default_attributes = {
        "height": 1.77,
        "location": None,  # a reference to the parent Elevator/Floor object
        "building": None,  # a reference to the parent building object
        "destination": None,  # a reference to the floor/elevator object that we are destined to
    }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = {}
        for key in BasePerson._default_attributes:
            self.set(key, BasePerson._default_attributes[key])
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BasePerson"))
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

        if name == "location":
            # if we are being added to a parent object then access its carrying attribute and add ourselves
            if value is not None:
                carrying = value.get("carrying")
                carrying.append(self)

                if(self.get("destination_floor") is not None):
                    value.add_to_request_queue(value.get("id"))

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
                    self.get("id"), destination_floor.get("id"), SOLE.LOG_INFO
                )
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
        SOLE.log(
            "[{}] BasePerson->location={} destination={}".format(
                self.get("id"),
                self.get("location").get("id"),
                self.get("destination_floor").get("id"),
                SOLE.LOG_INFO,
            )
        )
