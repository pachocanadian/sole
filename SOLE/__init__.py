# Define package list for this directory.
__all__ = ["Building", "Elevator", "Floor", "Person"]

import time
import re
import uuid

current_tick = 0

LOG_DEBUG = 1
LOG_INFO = 2
LOG_NOTICE = 4
LOG_WARNING = 8
LOG_ERR = 16
LOG_CRIT = 32
LOG_ALERT = 64
LOG_EMERG = 128

verbosity = LOG_NOTICE | LOG_WARNING | LOG_ERR | LOG_CRIT | LOG_ALERT | LOG_EMERG

tick_ratio_to_real_time = 10  # 10 ticks per real world second. 1m/s is 0.1m/t

_sole_id_log = dict()


def timestamp():
    """ Return a current time and tick as a string for use in logging. """
    return "[{0}] [{1:05d}]".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), current_tick
    )


def log(message, loglevel=LOG_NOTICE):
    """ Log a message to the console with timestamp. """
    if (loglevel & verbosity) > 0:
        print("{} {}".format(timestamp(), message))


def new_id(classref="UnspecifiedClass"):
    """ Define a new class id and return it and the count of its occurances. """
    key = re.sub("[^A-Z]", "", classref)
    key = key[0:2]

    if len(key) != 2:
        key = "UN"

    counter = 0
    if key in _sole_id_log:
        counter = _sole_id_log[key] + 1
        _sole_id_log[key] = counter
    else:
        counter = 1
        _sole_id_log[key] = counter

    return "%s-%05d" % (key, counter)
