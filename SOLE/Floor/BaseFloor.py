import uuid


class BaseFloor:
    def __init__(self, label=None):
        self._uuid = uuid.uuid1()
        self.label = label

    def uuid(self):
        return self._uuid

    def setLabel(self, label):
        self.label = label
