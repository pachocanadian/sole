#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time


# Simulation parameters
SOLE.log("Starting simulation")
startTime = time.time()

floor_labels = ["Lobby", 1, 2, 3]
floors = []
for fl in floor_labels:
    f = SOLE.Floor.SimpleFloor({"label": fl})
    floors.append(f)

initial_location = floor_labels[0]
elevator = SOLE.Elevator.SimpleElevator(
    {
        "floors": floors,
        "elevation": 0,
        "status": "waiting",
        "destination_floor": floors[3].get("id"),
    }
)

elevators = []
elevators.append(elevator)

SOLE.log("Creating initial building")
a = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": elevators})

for t in range(10):
    SOLE.current_tick += 1
    a.tick()

timeElapsed = time.time() - startTime

print(
    "Simulation started at: {}. \n Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
