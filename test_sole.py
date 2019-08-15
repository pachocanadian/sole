#

import pytest
import SOLE

# BEGIN BASEBUILDING TESTS

def test_BASEBUILDING_getset_string():
    a = SOLE.Building.BaseBuilding()
    v = 'var'
    a.set('test_string', v)
    assert (a.get('test_string') == v) 

def test_BASEBUILDING_getset_float():
    a = SOLE.Building.BaseBuilding()
    v = 3.14159
    a.set('test_float', v) 
    assert (a.get('test_float') == v)

def test_BASEBUILDING_getset_list():
    a = SOLE.Building.BaseBuilding()
    v = [1, 2, 3]
    a.set('test_list', v)
    assert (a.get('test_list') == v)

def test_BASEBUILDING_getset_dict():
    a = SOLE.Building.BaseBuilding()
    v = { 'a': 'b', 'c': 'd' }
    a.set('test_dict', v)
    assert (a.get('test_dict') == v)

def test_BASEBUILDING_getset_iscopy():
    a = SOLE.Building.BaseBuilding()
    ov = 'foo'
    a.set('test_iscopy', ov)
    nv = a.get('test_iscopy')
    assert (nv is ov)

# END BASEBUILDING TESTS

# BEGIN BASEELEVATOR TESTS

def test_BASEELEVATOR_getset_string():
    a = SOLE.Elevator.BaseElevator()
    v = 'var'
    a.set('test_string', v)
    assert (a.get('test_string') == v) 

def test_BASEELEVATOR_getset_float():
    a = SOLE.Elevator.BaseElevator()
    v = 3.14159
    a.set('test_float', v) 
    assert (a.get('test_float') == v)

def test_BASEELEVATOR_getset_list():
    a = SOLE.Elevator.BaseElevator()
    v = [1, 2, 3]
    a.set('test_list', v)
    assert (a.get('test_list') == v)

def test_BASEELEVATOR_getset_dict():
    a = SOLE.Elevator.BaseElevator()
    v = { 'a': 'b', 'c': 'd' }
    a.set('test_dict', v)
    assert (a.get('test_dict') == v)

def test_BASEELEVATOR_getset_iscopy():
    a = SOLE.Elevator.BaseElevator()
    ov = 'foo'
    a.set('test_iscopy', ov)
    nv = a.get('test_iscopy')
    assert (nv is ov)

# END BASEELEVATOR TESTS

# BEGIN BASEFLOOR TESTS

def test_BASEFLOOR_getset_string():
    a = SOLE.Floor.BaseFloor()
    v = 'var'
    a.set('test_string', v)
    assert (a.get('test_string') == v) 

def test_BASEFLOOR_getset_float():
    a = SOLE.Floor.BaseFloor()
    v = 3.14159
    a.set('test_float', v) 
    assert (a.get('test_float') == v)

def test_BASEFLOOR_getset_list():
    a = SOLE.Floor.BaseFloor()
    v = [1, 2, 3]
    a.set('test_list', v)
    assert (a.get('test_list') == v)

def test_BASEFLOOR_getset_dict():
    a = SOLE.Floor.BaseFloor()
    v = { 'a': 'b', 'c': 'd' }
    a.set('test_dict', v)
    assert (a.get('test_dict') == v)

def test_BASEFLOOR_getset_iscopy():
    a = SOLE.Floor.BaseFloor()
    ov = 'foo'
    a.set('test_iscopy', ov)
    nv = a.get('test_iscopy')
    assert (nv is ov)

# END BASEFLOOR TESTS

# BEGIN BASEPERSON TESTS

def test_BASEPERSON_getset_string():
    a = SOLE.Person.BasePerson()
    v = 'var'
    a.set('test_string', v)
    assert (a.get('test_string') == v) 

def test_BASEPERSON_getset_float():
    a = SOLE.Person.BasePerson()
    v = 3.14159
    a.set('test_float', v) 
    assert (a.get('test_float') == v)

def test_BASEPERSON_getset_list():
    a = SOLE.Person.BasePerson()
    v = [1, 2, 3]
    a.set('test_list', v)
    assert (a.get('test_list') == v)

def test_BASEPERSON_getset_dict():
    a = SOLE.Person.BasePerson()
    v = { 'a': 'b', 'c': 'd' }
    a.set('test_dict', v)
    assert (a.get('test_dict') == v)

def test_BASEPERSON_getset_iscopy():
    a = SOLE.Person.BasePerson()
    ov = 'foo'
    a.set('test_iscopy', ov)
    nv = a.get('test_iscopy')
    assert (nv is ov)

# END BASEPERSON TESTS


