import uuid


class BasePerson:
    def __init__(self):
        self._uuid = uuid.uuid1()

    def uuid(self):
        return self._uuid
