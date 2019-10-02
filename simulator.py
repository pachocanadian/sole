#!/usr/bin/env python3

from pprint import pprint
import SOLE
from SOLE.Building.SimpleBuilding import SimpleBuilding as Building
from SOLE.Elevator.SimpleElevator import SimpleElevator as Elevator
from SOLE.Floor.SimpleFloor import SimpleFloor as Floor
from SOLE.Person.SimplePerson import SimplePerson as Person
import time
import random

SOLE.verbosity = SOLE.LOG_NOTICE


def new_person(building):
    """ Return a new Person object with randomized destination and location. """

    # Randomize person's destination and location.
    floors = building.get("floors")
    location_floor = random.randint(0, len(floors) - 1)
    destination_floor = (random.randint(1, len(floors) - 1) + location_floor) % len(
        floors
    )

    p = Person(
        {
            "location": floors[location_floor],
            "destination_floor": floors[destination_floor],
        }
    )

    return p


# Simulation parameters
SOLE.log("Starting simulation")
startTime = time.time()

# Assign labels to floors.
floor_labels = ["Lobby", "1st Floor", "2nd Floor", "3rd Floor"]
floors = []
for fl in floor_labels:
    f = Floor({"label": fl})
    floors.append(f)

# Create an elevator.
initial_location = floor_labels[0]
elevator = Elevator(
        {"floors": floors, "elevation": 0, "status": "waiting", "destination_floor": None, "label": "Main Elevator"}
)

elevators = []
elevators.append(elevator)

# Create a building.
building = Building({"floors": floors, "elevators": elevators})

# Create people for simulation testing.
for t in range(999):
    if t % 100 == 10:
        new_person(building)
    SOLE.current_tick += 1
    building.tick()

# Summarize simulation.
timeElapsed = time.time() - startTime

SOLE.log(
    "Simulation started at: {}. Time elapsed: {}. Simulator time elapsed {} seconds.".format(
        time.strftime("%x %X", time.localtime(startTime)),
        timeElapsed,
        (SOLE.current_tick / SOLE.tick_ratio_to_real_time),
    )
)
