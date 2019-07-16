#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time

# Simulation parameters
startTime = time.time()

floorLabels = ["Lobby", 1, 2, 3]
floors = []
for floorLabel in floorLabels:
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    floors.append(f)

basic_elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "location": "Lobby", "status": "waiting"}
)

a = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": [basic_elevator]})

for t in range(10):
    a.tick()

timeElapsed = time.time() - startTime

print(
    "Simulation started at: {}. \n Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
