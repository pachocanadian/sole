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
            self._attributes[name] = value
            return self

    def get(self, name):
        """get(attr) will return attribute attr for the object or empty string if not"""
        if name in self._attributes:
            return self._attributes[name]
        else:
            return None
