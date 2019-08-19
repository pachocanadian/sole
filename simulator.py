#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time

SOLE.verbosity = SOLE.LOG_INFO | SOLE.LOG_NOTICE | SOLE.LOG_WARNING | SOLE.LOG_ERR | SOLE.LOG_CRIT | SOLE.LOG_ALERT | SOLE.LOG_EMERG

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
    {
        "floors": floors,
        "elevation": 0,
        "status": "waiting",
        "destination_floor": None
    }
)

elevator.add_to_request_queue(floors[3].get("id"))
elevator.add_to_request_queue(floors[1].get("id"))
elevator.add_to_request_queue(floors[2].get("id"))
elevator.add_to_request_queue(floors[0].get("id"))

elevators = []
elevators.append(elevator)

SOLE.log("Creating initial building")
building = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": elevators})

for t in range(50):
    SOLE.current_tick += 1
    building.tick()

timeElapsed = time.time() - startTime


SOLE.log("Simulation started at: {}. Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
