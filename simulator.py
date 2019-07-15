#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time

# Simulation parameters
startTime = time.clock()

floorLabels = ["Lobby", 1, 2, 3]
floors = []
for floorLabel in floorLabels:
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    print(f)
    floors.append(f)


basic_elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "location": "Lobby", "status": "waiting"}
)
print(basic_elevator)


# Instantiate starting objects
d = SOLE.Person.SimplePerson()
print(d)

e = SOLE.Person.SimplePerson()
print(e)

a = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": [basic_elevator]})
print(a)

timeElapsed = time.clock() - startTime

print(f"Simulation started at: {startTime}. \n Time elapsed: {timeElapsed}")