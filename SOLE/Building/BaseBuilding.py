import SOLE

class BaseBuilding:
    default_attributes = {"height": None, "floors": [], "elevators": [] }

    def __init__(self, attributes=None):
        """init() with no parameters or init(dict) can specify a dictionary of attributes"""
        self.attribute = {}
        for key in BaseBuilding.default_attributes:
            self.set(key, BaseBuilding.default_attributes[key])
        if attributes is not None:
            for key in attributes:
                self.set(key, attributes[key])
        self.set("id", SOLE.new_id("BaseBuilding"))

        running_height = 0
        floors = self.get("floors")
        if(type(floors) == list):
            for f in floors:
                floor_id = f.get("id")
                f.set("elevation", running_height)
                running_height += f.get("height")
                f.set("elevation_top", running_height)
                f.set("building", self)
            self.set("height", running_height)


    def __str__(self):
        """allow print() to function in some intelligible way"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""
        self.attribute[name] = value
        return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self.attribute:
            return self.attribute[name]
        else:
            return None

    def elevation_of(self, object_id):
        eo = self.get("_elevation_of")
        if(object_id is None):
            return 0

        if object_id in eo:
            return eo[object_id]
        else:
            return None

    def at_elevation(self, height):
        ae = self.get("_at_elevation")
        if height in ae:
            return ae[height]
        else:
            return None

    def ref_to(self, object_id):
        rt = self.get("_ref_to")
        if object_id in rt:
            return rt[object_id]
        else:
            return None

    def rebuild_internal_tracking(self):
        """rebuild_internal_tracking() maintains height tables. it is called every tick()"""
        _elevation_of = dict()
        _at_elevation = dict()
        _ref_to = dict()
        running_height = 0

        floors = self.get("floors")
        if(type(floors) == list and len(floors) > 0):
            for f in floors:
                floor_id = f.get("id")
                floor_elevation = f.get("elevation")
                _ref_to[floor_id] = f
                _elevation_of[floor_id] = floor_elevation
                _at_elevation[floor_elevation] = floor_id
                carrying = f.get("carrying")
                if(type(carrying) == list and len(carrying) > 0):
                    for p in carrying:
                        person_id = p.get("id")
                        person_elevation = p.get("elevation")
                        _ref_to[person_id] = p
                        _elevation_of[person_id] = person_elevation

        self.set("_elevation_of", _elevation_of)
        self.set("_at_elevation", _at_elevation)

        elevators = self.get("elevators")
        if(type(elevators) == list):
            for e in elevators:
                elevator_id = e.get("id")
                elevator_elevation = e.get("elevation")
                _ref_to[elevator_id] = e
                _elevation_of[elevator_id] = elevator_elevation
                carrying = e.get("carrying")
                if(type(carrying) == list and len(carrying) > 0):
                    for p in carrying:
                        person_id = p.get("id")
                        person_elevation = p.get("elevation")
                        _ref_to[person_id] = p
                        _elevation_of[person_id] = person_elevation

                e.set("building", self)

        self.set("_ref_to", _ref_to)

    def tick(self):
        """tick() will advance one step for this object and any/all objects contained by it"""
        SOLE.log("[{}] BaseBuilding->tick()".format(self.get("id")), SOLE.LOG_INFO)
        self.rebuild_internal_tracking()
        for f in self.get("floors"):
            f.tick()
        for e in self.get("elevators"):
            e.tick()
        # for e in elevator: e.tick()
        # for p in people: p.tick()
        # for f in floors: f.tick()
        return
