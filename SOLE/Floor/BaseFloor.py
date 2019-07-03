import uuid


class BaseFloor:
    def __init__(self, label=None):
        self._id = uuid.uuid1()
        self.label = label

    def id(self):
        return self._id

    def setLabel(self, label):
        self.label = label
