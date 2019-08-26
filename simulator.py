#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time
import random

SOLE.verbosity = (
    SOLE.LOG_INFO
    | SOLE.LOG_NOTICE
    | SOLE.LOG_WARNING
    | SOLE.LOG_ERR
    | SOLE.LOG_CRIT
    | SOLE.LOG_ALERT
    | SOLE.LOG_EMERG
)

# Simulation parameters
SOLE.log("Starting simulation")
startTime = time.time()

# Assign labels to floors.
floor_labels = ["Lobby", 1, 2, 3]
floors = []
for fl in floor_labels:
    f = SOLE.Floor.SimpleFloor({"label": fl})
    floors.append(f)

initial_location = floor_labels[0]
elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "elevation": 0, "status": "waiting", "destination_floor": None}
)

elevators = []
elevators.append(elevator)

building = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": elevators})


for t in range(999):
    if(t % 100 == 0):
        p = SOLE.Person.BasePerson()
        p.set("destination_floor", building.get("floors")[0])
        p.set("location", building.get("floors")[random.randint(1,3)])
    SOLE.current_tick += 1
    building.tick()

timeElapsed = time.time() - startTime


SOLE.log(
    "Simulation started at: {}. Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
