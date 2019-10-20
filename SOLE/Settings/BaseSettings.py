import SOLE
import re


class BaseSettings:
    def __init__(self, variable_definitions):
        """init() requires a dict of variable definitions"""
        self._variable_definitions = variable_definitions
        self._attributes = {}
        for key in self._variable_definitions:
            if "default" in self._variable_definitions[key]:
                self.set(key, self._variable_definitions[key]["default"])

    def set(self, name, value):
        """set() will set the given attribute for the object. Will perform basic sanity checks on the attribute itself."""

        if name in self._variable_definitions:
            _type = self._variable_definitions[name]["type"]
            if _type == "float":
                if type(value) == int:
                    value = float(value)
                assert (
                    type(value) == float
                ), "Named attribute {} of value {} of type {} must be a float()".format(
                    name, value, _type
                )
            elif _type == "string":
                assert (
                    type(value) == str
                ), "Named attribute {} of value {} of type {} must be a str()".format(
                    name, value, _type
                )
            elif _type == "building":
                pass
            elif _type == "floor":
                pass
            elif _type == "dict":
                assert (
                    type(value) == dict
                ), "Named attribute {} of value {} of type {} must be a dict()".format(
                    name, value, _type
                )
            elif _type == "list":
                assert (
                    type(value) == list
                ), "Named attribute {} of value {} of type {} must be a list()".format(
                    name, value, _type
                )
            elif _type == "boolean":
                assert (
                    type(value) == bool
                ), "Named attribute {} of value {} of type {} must be a bool()".format(
                    name, value, _type
                )
            elif _type == "reference":
                pass
            else:
                raise Exception("unmatched variable type {}".format(_type))

            if "validation" in self._variable_definitions[name]:
                _validation = self._variable_definitions[name]["validation"]
                if _validation == "":
                    pass
                elif _validation == "gt_zero":
                    assert (
                        value > 0
                    ), "Named attribute {} of value {} of type {} must be greater than zero".format(
                        name, value, _type
                    )
                elif _validation == "lt_zero":
                    assert (
                        value < 0
                    ), "Named attribute {} of value {} of type {} must be less than zero".format(
                        name, value, _type
                    )
                elif _validation == "is_percent":
                    assert (value >= 0) and (
                        value <= 1.0
                    ), "Named attribute {} of value {} of type {} must be percentage between 0.00 and 1.00".format(
                        name, value, _type
                    )

                else:
                    assert (
                        False
                    ), "Named attribute {} of value {} of type {} has invalid validation type {}".format(
                        name, value, _type, _validation
                    )

            self._attributes[name] = value
            return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self._attributes:
            return self._attributes[name]
        else:
            return None

    def __str__(self):
        out = ""
        for key in self._attributes:
            _type = self._variable_definitions[key]["type"]
            if _type == "reference":
                out += "{}: REFERENCE<{}>,".format(key, self.get(key).get("id"))
            elif _type == "floor":
                out += "{}: FLOOR<{}>,".format(key, self.get(key).get("id"))
            elif _type == "building":
                out += "{}: BUILDING<{}>,".format(key, self.get(key).get("id"))
            else:
                out += "{}: {},".format(key, self.get(key))
        return out
