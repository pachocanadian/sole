#

import pytest
import SOLE

# BUILDING
import SOLE.Building.BaseBuilding
import SOLE.Building.SimpleBuilding

# ELEVATOR
import SOLE.Elevator.BaseElevator
import SOLE.Elevator.SimpleElevator

# FLOOR
import SOLE.Floor.BaseFloor
import SOLE.Floor.SimpleFloor

# PERSON
import SOLE.Person.BasePerson
import SOLE.Person.SimplePerson

###### BEGIN BUILDING TESTS ######
###
### BEGIN BASEBUILDING TESTS
###


def test_BASEBUILDING_getset_string():
    a = SOLE.Building.BaseBuilding()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEBUILDING_getset_float():
    a = SOLE.Building.BaseBuilding()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEBUILDING_getset_list():
    a = SOLE.Building.BaseBuilding()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEBUILDING_getset_dict():
    a = SOLE.Building.BaseBuilding()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEBUILDING_getset_iscopy():
    a = SOLE.Building.BaseBuilding()
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
    a = SOLE.Building.SimpleBuilding()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEBUILDING_getset_float():
    a = SOLE.Building.SimpleBuilding()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEBUILDING_getset_list():
    a = SOLE.Building.SimpleBuilding()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEBUILDING_getset_dict():
    a = SOLE.Building.SimpleBuilding()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEBUILDING_getset_iscopy():
    a = SOLE.Building.SimpleBuilding()
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
    a = SOLE.Elevator.BaseElevator()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEELEVATOR_getset_float():
    a = SOLE.Elevator.BaseElevator()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEELEVATOR_getset_list():
    a = SOLE.Elevator.BaseElevator()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEELEVATOR_getset_dict():
    a = SOLE.Elevator.BaseElevator()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEELEVATOR_getset_iscopy():
    a = SOLE.Elevator.BaseElevator()
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
    a = SOLE.Elevator.SimpleElevator()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEELEVATOR_getset_float():
    a = SOLE.Elevator.SimpleElevator()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEELEVATOR_getset_list():
    a = SOLE.Elevator.SimpleElevator()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEELEVATOR_getset_dict():
    a = SOLE.Elevator.SimpleElevator()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEELEVATOR_getset_iscopy():
    a = SOLE.Elevator.SimpleElevator()
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
    a = SOLE.Floor.BaseFloor()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEFLOOR_getset_float():
    a = SOLE.Floor.BaseFloor()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEFLOOR_getset_list():
    a = SOLE.Floor.BaseFloor()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEFLOOR_getset_dict():
    a = SOLE.Floor.BaseFloor()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEFLOOR_getset_iscopy():
    a = SOLE.Floor.BaseFloor()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returing a copy rather than the original object"


###
### END BASEFLOOR TESTS
###
### BEGIN SIMPLEFLOOR TESTS
###


def test_SIMPLEFLOOR_getset_string():
    a = SOLE.Floor.SimpleFloor()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEFLOOR_getset_float():
    a = SOLE.Floor.SimpleFloor()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEFLOOR_getset_list():
    a = SOLE.Floor.SimpleFloor()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEFLOOR_getset_dict():
    a = SOLE.Floor.SimpleFloor()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEFLOOR_getset_iscopy():
    a = SOLE.Floor.SimpleFloor()
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
    a = SOLE.Person.BasePerson()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_BASEPERSON_getset_float():
    a = SOLE.Person.BasePerson()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_BASEPERSON_getset_list():
    a = SOLE.Person.BasePerson()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_BASEPERSON_getset_dict():
    a = SOLE.Person.BasePerson()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_BASEPERSON_getset_iscopy():
    a = SOLE.Person.BasePerson()
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
    a = SOLE.Person.SimplePerson()
    v = "var"
    a.set("test_string", v)
    assert a.get("test_string") == v, "set/get don't match for string type"


def test_SIMPLEPERSON_getset_float():
    a = SOLE.Person.SimplePerson()
    v = 3.14159
    a.set("test_float", v)
    assert a.get("test_float") == v, "set/get don't match for float type"


def test_SIMPLEPERSON_getset_list():
    a = SOLE.Person.SimplePerson()
    v = [1, 2, 3]
    a.set("test_list", v)
    assert a.get("test_list") == v, "set/get don't match for list type"


def test_SIMPLEPERSON_getset_dict():
    a = SOLE.Person.SimplePerson()
    v = {"a": "b", "c": "d"}
    a.set("test_dict", v)
    assert a.get("test_dict") == v, "set/get don't match for dict type"


def test_SIMPLEPERSON_getset_iscopy():
    a = SOLE.Person.SimplePerson()
    ov = "foo"
    a.set("test_iscopy", ov)
    nv = a.get("test_iscopy")
    assert nv is ov, "set/get are returning a copy rather than the original object"


###
### END SIMPLEPERSON TESTS
###
###### END PERSON TESTS ######
