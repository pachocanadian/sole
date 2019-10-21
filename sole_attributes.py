#!/usr/bin/env python3

from pprint import pprint
import SOLE
from SOLE.Building.SimpleBuilding import SimpleBuilding as Building
from SOLE.Elevator.SimpleElevator import SimpleElevator as Elevator
from SOLE.Floor.SimpleFloor import SimpleFloor as Floor
from SOLE.Person.SimplePerson import SimplePerson as Person

building = Building()
elevator = Elevator()
floor = Floor()
person = Person()

print("# Default attributes for SOLE objects")

print("\n")
print("### {}\n".format("SOLE.Building.BaseBuilding"))
print("|*{}*|*{}*|*{}*|".format("Attribute", "Description", "Default Value"))
print("| --- | --- | --- |")
for attribute in building.settings._variable_definitions:
    print(
        "|`{}`|{}|{}|".format(
            attribute,
            building.settings._variable_definitions[attribute]["comment"],
            building.settings._variable_definitions[attribute]["default"],
        )
    )

print("\n")
print("### {}\n".format("SOLE.Building.BaseElevator"))
print("|*{}*|*{}*|*{}*|".format("Attribute", "Description", "Default Value"))
print("| --- | --- | --- |")
for attribute in elevator.settings._variable_definitions:
    print(
        "|`{}`|{}|{}|".format(
            attribute,
            elevator.settings._variable_definitions[attribute]["comment"],
            elevator.settings._variable_definitions[attribute]["default"],
        )
    )

print("\n")
print("### {}\n".format("SOLE.Building.BaseFloor"))
print("|*{}*|*{}*|*{}*|".format("Attribute", "Description", "Default Value"))
print("| --- | --- | --- |")
for attribute in floor.settings._variable_definitions:
    print(
        "|`{}`|{}|{}|".format(
            attribute,
            floor.settings._variable_definitions[attribute]["comment"],
            floor.settings._variable_definitions[attribute]["default"],
        )
    )

print("\n")
print("### {}\n".format("SOLE.Building.BasePerson"))
print("|*{}*|*{}*|*{}*|".format("Attribute", "Description", "Default Value"))
print("| --- | --- | --- |")
for attribute in person.settings._variable_definitions:
    print(
        "|`{}`|{}|{}|".format(
            attribute,
            person.settings._variable_definitions[attribute]["comment"],
            person.settings._variable_definitions[attribute]["default"],
        )
    )
