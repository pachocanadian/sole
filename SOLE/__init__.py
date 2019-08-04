__all__ = ["Building", "Elevator", "Floor", "Person"]

import time
import re
import uuid
from SOLE.Building import *
from SOLE.Elevator import *
from SOLE.Floor import *
from SOLE.Person import *

current_tick = 0

sole_id_log = dict()


def timestamp():
    return "[{0}] [{1:05d}]".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), current_tick
    )


def log(message, loglevel=4):
    print("{} {}".format(timestamp(), message))


def new_id(classref="UnspecifiedClass"):
    key = re.sub("[^A-Z]", "", classref)
    key = key[0:2]

    if len(key) != 2:
        key = "UN"

    counter = 0
    if key in sole_id_log:
        counter = sole_id_log[key] + 1
        sole_id_log[key] = counter
    else:
        counter = 1
        sole_id_log[key] = counter

    return "%s-%05d-%s" % (key, counter, str(uuid.uuid4()))
