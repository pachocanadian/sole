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


def test_BASEBUILDING_new():
    a = BaseBuilding()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END BASEBUILDING TESTS
###
### BEGIN SIMPLEBUILDING TESTS
###


def test_SIMPLEBUILDING_new():
    a = SimpleBuilding()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END SIMPLEBUILDING TESTS
###
###### END BUILDING TESTS ######

###### BEGIN ELEVATOR TESTS ######
###
### BEGIN BASEELEVATOR TESTS
###


def test_BASEELEVATOR_new():
    a = BaseElevator()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END BASEELEVATOR TESTS
###
### BEGIN SIMPLEELEVATOR TESTS
###


def test_SIMPLEELEVATOR_new():
    a = SimpleElevator()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END SIMPLEELEVATOR TESTS
###
###### END ELEVATOR TESTS ######

###### BEGIN FLOOR TESTS ######
###
### BEGIN BASEFLOOR TESTS


def test_BASEFLOOR_new():
    a = BaseFloor()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END BASEFLOOR TESTS
###
### BEGIN SIMPLEFLOOR TESTS
###


def test_SIMPLEFLOOR_new():
    a = SimpleFloor()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END SIMPLEFLOOR TESTS
###
###### END FLOOR TESTS ######

###### BEGIN PERSON TESTS ######
###
### BEGIN BASEPERSON TESTS
###


def test_BASEPERSON_new():
    a = BasePerson()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END BASEPERSON TESTS
###
### BEGIN SIMPLEPERSON TESTS
###


def test_SIMPLEPERSON_new():
    a = SimplePerson()
    id = a.get("id")
    assert type(id) == str and len(id) > 0, "can't create object"


###
### END SIMPLEPERSON TESTS
###
###### END PERSON TESTS ######

### BEGIN BASESETTINGS TESTS
###


##### STRING TYPE


def test_BASESETTINGS_getset_string():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASESETTINGS_getset_string_notfloat():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = 1.00
    with pytest.raises(AssertionError, match="test_string.*string") as excinfo:
        a.set("test_string", v)


def test_BASESETTINGS_getset_string_notint():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = 1
    with pytest.raises(AssertionError, match="test_string.*string") as excinfo:
        a.set("test_string", v)


def test_BASESETTINGS_getset_string_notlist():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = []
    with pytest.raises(AssertionError, match="test_string.*string") as excinfo:
        a.set("test_string", v)


def test_BASESETTINGS_getset_string_notdict():
    a = BaseSettings({"test_string": {"type": "string"}})
    v = {}
    with pytest.raises(AssertionError, match="test_string.*string") as excinfo:
        a.set("test_string", v)


##### FLOAT TYPE


def test_BASESETTINGS_getset_float():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASESETTINGS_getset_float_notstring():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = "foo"
    with pytest.raises(AssertionError, match="test_float.*float") as excinfo:
        a.set("test_float", v)


def test_BASESETTINGS_getset_float_intok():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = 3
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get doesn't cast int type"


def test_BASESETTINGS_getset_float_notlist():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = []
    with pytest.raises(AssertionError, match="test_float.*float") as excinfo:
        a.set("test_float", v)


def test_BASESETTINGS_getset_float_notdict():
    a = BaseSettings({"test_float": {"type": "float"}})
    v = {}
    with pytest.raises(AssertionError, match="test_float.*float") as excinfo:
        a.set("test_float", v)


##### LIST TYPE


def test_BASESETTINGS_getset_list():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASESETTINGS_getset_list_notstring():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = "foo"
    with pytest.raises(AssertionError, match="test_list.*list") as excinfo:
        a.set("test_list", v)


def test_BASESETTINGS_getset_list_notfloat():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = 1.00
    with pytest.raises(AssertionError, match="test_list.*list") as excinfo:
        a.set("test_list", v)


def test_BASESETTINGS_getset_list_notint():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = 1
    with pytest.raises(AssertionError, match="test_list.*list") as excinfo:
        a.set("test_list", v)


def test_BASESETTINGS_getset_list_notdict():
    a = BaseSettings({"test_list": {"type": "list"}})
    v = {}
    with pytest.raises(AssertionError, match="test_list.*list") as excinfo:
        a.set("test_list", v)


##### DICT TYPE


def test_BASESETTINGS_getset_dict():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASESETTINGS_getset_dict_notstring():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = "foo"
    with pytest.raises(AssertionError, match="test_dict.*dict") as excinfo:
        a.set("test_dict", v)


def test_BASESETTINGS_getset_dict_notfloat():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = 1.00
    with pytest.raises(AssertionError, match="test_dict.*dict") as excinfo:
        a.set("test_dict", v)


def test_BASESETTINGS_getset_dict_notint():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = 1
    with pytest.raises(AssertionError, match="test_dict.*dict") as excinfo:
        a.set("test_dict", v)


def test_BASESETTINGS_getset_dict_notlist():
    a = BaseSettings({"test_dict": {"type": "dict"}})
    v = []
    with pytest.raises(AssertionError, match="test_dict.*dict") as excinfo:
        a.set("test_dict", v)


##### COPY


def test_BASESETTINGS_getset_iscopy():
    a = BaseSettings({"test_iscopy": {"type": "string"}})
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returning a copy rather than the original object"


##### DEFAULTS


def test_BASESETTINGS_getset_defaultsdosomething():
    a = BaseSettings({"test_default1": {"type": "string", "default": "value1"}})
    ov = "value1"
    nv = a.get("test_default1")
    assert nv == ov, "defaults are populating correctly in absence of a set"


def test_BASESETTINGS_getset_defaultsdontoverride():
    a = BaseSettings({"test_default2": {"type": "string", "default": "value2"}})
    ov = "value1"
    a.set("test_default2", ov)
    nv = a.get("test_default2")
    assert nv == ov, "set is overriding default arguments when supplied"


###### VALIDATION


def test_BASESETTINGS_validation_gt_zero_ok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "gt_zero"}})
    v = 1.00
    a.set("test_float", v)


def test_BASESETTINGS_validation_gt_zero_notok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "gt_zero"}})
    v = -1.00
    with pytest.raises(AssertionError, match="test_float") as excinfo:
        a.set("test_float", v)


def test_BASESETTINGS_validation_lt_zero_ok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "lt_zero"}})
    v = -1.00
    a.set("test_float", v)


def test_BASESETTINGS_validation_lt_zero_notok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "lt_zero"}})
    v = 1.00
    with pytest.raises(AssertionError, match="test_float") as excinfo:
        a.set("test_float", v)


def test_BASESETTINGS_validation_is_percent_ok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "is_percent"}})
    for i in range(100):
        v = i / 100.00
        a.set("test_float", v)


def test_BASESETTINGS_validation_is_percent_notok():
    a = BaseSettings({"test_float": {"type": "float", "validation": "is_percent"}})
    v = 1.01
    with pytest.raises(AssertionError, match="test_float") as excinfo:
        a.set("test_float", v)


###
### END BASESETTINGS TESTS
#
