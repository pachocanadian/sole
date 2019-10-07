import SOLE
import re


class BaseSettings:
    def __init__(self, variable_definitions):
        """init() requires a dict of variable definitions"""
        self._variable_definitions = variable_definitions
        self._attributes = {}

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""

        if name in self._variable_definitions:
            _type = self._variable_definitions[name]["type"]
            if _type == "float":
                assert type(value) == float, "Value must be a float()"
            elif _type == "string":
                assert type(value) == str, "Value must be a str()"
            elif _type == "floor":
                pass
            elif _type == "dict":
                assert type(value) == dict, "Value must be a dict()"
            elif _type == "list":
                assert type(value) == list, "Value must be a list()"
            else:
                raise Exception("unmatched variable type {}".format(_type))

            if "validation" in self._variable_definitions[name]:
                _validation = self._variable_definitions[name]["validation"]
                if _validation == "gt_zero":
                    assert value > 0, "Value must be greater than zero"
                else:
                    pass

            self._attributes[name] = value
            return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self._attributes:
            return self._attributes[name]
        else:
            return None
