#

import pytest
import SOLE

# BUILDING
from SOLE.Building.BaseBuilding import BaseBuilding
from SOLE.Building.SimpleBuilding import SimpleBuilding

# ELEVATOR
from SOLE.Elevator.BaseElevator import BaseElevator
from SOLE.Elevator.SimpleElevator import SimpleElevator

# FLOOR
from SOLE.Floor.BaseFloor import BaseFloor
from SOLE.Floor.SimpleFloor import SimpleFloor

# PERSON
from SOLE.Person.BasePerson import BasePerson
from SOLE.Person.SimplePerson import SimplePerson

# SETTINGS
from SOLE.Settings.BaseSettings import BaseSettings


###### BEGIN BUILDING TESTS ######
###
### BEGIN BASEBUILDING TESTS
###


def test_BASEBUILDING_getset_string():
    a = BaseBuilding()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEBUILDING_getset_float():
    a = BaseBuilding()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEBUILDING_getset_list():
    a = BaseBuilding()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEBUILDING_getset_dict():
    a = BaseBuilding()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEBUILDING_getset_iscopy():
    a = BaseBuilding()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END BASEBUILDING TESTS
###
### BEGIN SIMPLEBUILDING TESTS
###


def test_SIMPLEBUILDING_getset_string():
    a = SimpleBuilding()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEBUILDING_getset_float():
    a = SimpleBuilding()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEBUILDING_getset_list():
    a = SimpleBuilding()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEBUILDING_getset_dict():
    a = SimpleBuilding()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEBUILDING_getset_iscopy():
    a = SimpleBuilding()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END SIMPLEBUILDING TESTS
###
###### END BUILDING TESTS ######

###### BEGIN ELEVATOR TESTS ######
###
### BEGIN BASEELEVATOR TESTS
###


def test_BASEELEVATOR_getset_string():
    a = BaseElevator()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEELEVATOR_getset_float():
    a = BaseElevator()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEELEVATOR_getset_list():
    a = BaseElevator()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEELEVATOR_getset_dict():
    a = BaseElevator()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEELEVATOR_getset_iscopy():
    a = BaseElevator()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END BASEELEVATOR TESTS
###
### BEGIN SIMPLEELEVATOR TESTS
###


def test_SIMPLEELEVATOR_getset_string():
    a = SimpleElevator()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEELEVATOR_getset_float():
    a = SimpleElevator()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEELEVATOR_getset_list():
    a = SimpleElevator()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEELEVATOR_getset_dict():
    a = SimpleElevator()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEELEVATOR_getset_iscopy():
    a = SimpleElevator()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END SIMPLEELEVATOR TESTS
###
###### END ELEVATOR TESTS ######

###### BEGIN FLOOR TESTS ######
###
### BEGIN BASEFLOOR TESTS


def test_BASEFLOOR_getset_string():
    a = BaseFloor()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEFLOOR_getset_float():
    a = BaseFloor()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEFLOOR_getset_list():
    a = BaseFloor()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEFLOOR_getset_dict():
    a = BaseFloor()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEFLOOR_getset_iscopy():
    a = BaseFloor()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


def test_BASEFLOOR_getset_diffsaredifferent():
    a = BaseFloor()
    b = BaseFloor()
    pre_av = "foo"
    pre_bv = "bar"
    a.set("test_unique", pre_av)
    b.set("test_unique", pre_bv)
    post_av = a.get("test_unique")
    post_bv = b.get("test_unique")
    assert (
        post_av != post_bv
    ), "set/get are returning different return values on objects with different initial set values"


###
### END BASEFLOOR TESTS
###
### BEGIN SIMPLEFLOOR TESTS
###


def test_SIMPLEFLOOR_getset_string():
    a = SimpleFloor()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEFLOOR_getset_float():
    a = SimpleFloor()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEFLOOR_getset_list():
    a = SimpleFloor()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEFLOOR_getset_dict():
    a = SimpleFloor()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEFLOOR_getset_iscopy():
    a = SimpleFloor()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END SIMPLEFLOOR TESTS
###
###### END FLOOR TESTS ######

###### BEGIN PERSON TESTS ######
###
### BEGIN BASEPERSON TESTS
###


def test_BASEPERSON_getset_string():
    a = BasePerson()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEPERSON_getset_float():
    a = BasePerson()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEPERSON_getset_list():
    a = BasePerson()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEPERSON_getset_dict():
    a = BasePerson()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEPERSON_getset_iscopy():
    a = BasePerson()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returning a copy rather than the original object"


###
### END BASEPERSON TESTS
###
### BEGIN SIMPLEPERSON TESTS
###


def test_SIMPLEPERSON_getset_string():
    a = SimplePerson()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEPERSON_getset_float():
    a = SimplePerson()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEPERSON_getset_list():
    a = SimplePerson()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEPERSON_getset_dict():
    a = SimplePerson()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEPERSON_getset_iscopy():
    a = SimplePerson()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returning a copy rather than the original object"


###
### END SIMPLEPERSON TESTS
###
###### END PERSON TESTS ######

### BEGIN BASESETTINGS TESTS
###


def test_BASESETTINGS_getset_string():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASESETTINGS_getset_float():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASESETTINGS_getset_list():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASESETTINGS_getset_dict():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASESETTINGS_getset_iscopy():
    a = BaseSettings({"test_iscopy": {"type": "string"}})
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returning a copy rather than the original object"


###
### END BASESETTINGS TESTS
#
