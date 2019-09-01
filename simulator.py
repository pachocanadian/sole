#!/usr/bin/env python3

from pprint import pprint
import SOLE
import time
import random

SOLE.verbosity = SOLE.LOG_NOTICE


def new_person():
    """ Return a new Person object with randomized destination and location. """
    p = SOLE.Person.BasePerson()

    # Randomize person's destination and location.
    with building.get("floors") as floors:
        p.set("destination_floor", floors[random.randint(0, len(floors))])
        p.set("location", floors[random.randint(0, len(floors))])

    return p


# Simulation parameters
SOLE.log("Starting simulation")
startTime = time.time()

# Assign labels to floors.
floor_labels = ["Lobby", "1st Floor", "2nd Floor", "3rd Floor"]
floors = []
for fl in floor_labels:
    f = SOLE.Floor.SimpleFloor({"label": fl})
    floors.append(f)

# Create an elevator.
initial_location = floor_labels[0]
elevator = SOLE.Elevator.SimpleElevator(
    {"floors": floors, "elevation": 0, "status": "waiting", "destination_floor": None}
)

elevators = []
elevators.append(elevator)

# Create a building.
building = SOLE.Building.SimpleBuilding({"floors": floors, "elevators": elevators})

# Create people for simulation testing.
for t in range(999):
    if t % 100 == 0:
        destination_floor = building.get("floors")[0]
        location = building.get("floors")[random.randint(1, 3)]
        p = SOLE.Person.BasePerson(
            {"destination_floor": destination_floor, "location": location}
        )
    SOLE.current_tick += 1
    building.tick()


# Summarize simulation.
timeElapsed = time.time() - startTime

SOLE.log(
    "Simulation started at: {}. Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
