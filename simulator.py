#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time


# Simulation parameters
SOLE.log("Starting simulation")
startTime = time.time()

floorLabels = ["Lobby", 1, 2, 3]
floors = []
for floorLabel in floorLabels:
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    floors.append(f)

initialLocation = floorLabels[0]
elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "elevation": 0, "status": "waiting", "destinationFloor": 3}
)

SOLE.log("Creating initial building")
a = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": [elevator]})

for t in range(10):
    SOLE.current_tick += 1
    a.tick()

timeElapsed = time.time() - startTime

print(
    "Simulation started at: {}. \n Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
