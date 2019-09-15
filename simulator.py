#!/usr/bin/env python3

from pprint import pprint
import SOLE
import SOLE.Building.SimpleBuilding
import SOLE.Elevator.SimpleElevator
import SOLE.Floor.SimpleFloor
import SOLE.Person.SimplePerson
import time
import random

SOLE.verbosity = SOLE.LOG_NOTICE


def new_person(building):
    """ Return a new Person object with randomized destination and location. """

    # Randomize person's destination and location.
    floors = building.get("floors")
    location_floor = random.randint(0, len(floors) - 1)
    destination_floor = (random.randint(0, len(floors) - 2) + location_floor) % len(
        floors
    )
    p = SOLE.Person.SimplePerson(
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
        new_person(building)
    SOLE.current_tick += 1
    building.tick()


# Test SpeakerPerson -- Needs fix

# speaker = SOLE.Person.SpeakerPerson
# for i in range(10):
#    speaker.speak_positive()


# Summarize simulation.
timeElapsed = time.time() - startTime

SOLE.log(
    "Simulation started at: {}. Time elapsed: {}".format(
        time.strftime("%x %X", time.localtime(startTime)), timeElapsed
    )
)
