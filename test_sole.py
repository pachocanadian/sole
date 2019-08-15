#

import pytest
import SOLE

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
