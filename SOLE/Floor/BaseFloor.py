import uuid


class BaseFloor:
    def __init__(self):
        self._id = uuid.uuid1()

    def id(self):
        return self._id
