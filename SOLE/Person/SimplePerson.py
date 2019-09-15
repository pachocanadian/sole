import SOLE
from SOLE.Person.BasePerson import BasePerson


class SimplePerson(BasePerson):
    def __init__(self, attributes=None):
        super().__init__(attributes)
        SOLE.log("[{}] SimplePerson->created".format(self.get("id")), SOLE.LOG_INFO)

    pass
