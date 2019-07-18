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
    SOLE.log("Creating floor {}".format(floorLabel))
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    floors.append(f)

initialLocation = floorLabels[0]
SOLE.log("Creating elevator with initial location {}".format(initialLocation))
basic_elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "elevation": 0, "status": "waiting", "destinationFloor": 3}
)

SOLE.log("Creating initial building")
a = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": [basic_elevator]})

for t in range(10):
    SOLE.current_tick += 1
    a.tick()

list_of_floors = a.get("floors")
for f in list_of_floors:
    print(f)
#    print(
#        "Floor {} {} has a height of {}, a bottom elevation of {} and a top elevation of {}".format(
#            f.get("uuid"),
#           f.get("label"),
#           f.get("height"),
#           f.get("elevation"),
#           f.get("elevation_top"),
#       )
#   )

timeElapsed = time.time() - startTime

print(
    "Simulation started at: {}. \n Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
