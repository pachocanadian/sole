import uuid


class BaseElevator:
    def __init__(self):
        self._id = uuid.uuid1()

    def id(self):
        return self._id
