__all__ = ["Building", "Elevator", "Floor", "Person"]

import time
import uuid
from SOLE.Building import *
from SOLE.Elevator import *
from SOLE.Floor import *
from SOLE.Person import *

current_tick = 0


def timestamp():
    return "[{0}] [{1:05d}]".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), current_tick
    )


def log(message, loglevel=4):
    print("{} {}".format(timestamp(), message))

def new_id():
    return uuid.uuid1()
