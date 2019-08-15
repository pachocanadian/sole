A simulator is made up of four main classes:

* Building
* Floor
* Elevator
* Person

## Building

| Attribute | Description |
| --------- | ----------- |
| ``id`` | string, system generated and guaranteed unique |
| ``label`` | string, friendly description of object |
| ``floors`` | list of BaseFloor-capable objects |
| ``elevator`` | list of BaseElevator-capable objects |
| ``elevation_of(id)`` | float, returns height of the associated `id` |

## Floor

| Attribute | Description |
| --------- | ----------- |
| ``id`` | string, system generated and guaranteed unique |
| ``label`` | string, friendly description of object |
| ``height`` | float, in metres; overall height of object |
| ``elevation`` | float, in metres; elevation of bottom-most point of object |
| ``elevation_top`` | float, in metres; elevation of bottom-most point of object |
| ``carrying`` | list of BasePerson-capable objects |

## Elevator

| Attribute | Description |
| --------- | ----------- |
| ``id`` | string, system generated and guaranteed unique |
| ``label`` | string, friendly description of object |
| ``height`` | float, in metres; overall height of object |
| ``elevation`` | float, in metres; elevation of bottom-most point of object |
| ``velocity`` | float, in metres/second; positive speed means moving up, negative means moving down, 0 at rest |
| ``maximum_up_speed`` | unsigned float, in metres/second; indicates maximum absolute speed upwards |
| ``maximum_down_speed`` | unsigned float, in metres/second; indicates maximum absolute speed downwards |
| ``destination_floor`` | string, references a floor ``id`` |
| ``carrying`` | list of BasePerson-capable objects |
| ``building`` | BaseBuilding-capable object which elevator is contained within |

* An elevator connects a non-empty list of at least two floors

## Person

| Attribute | Description |
| --------- | ----------- |
| ``id`` | string, system generated and guaranteed unique |
| ``label`` | string, friendly description of object |
| ``height`` | float, in metres; overall height of object |
| ``location`` | string, references the id of the floor/elevator that the person is contained within |

## SOLE

The base module for SOLE provides three functions to help support:

* ``timestamp()`` - this returns a time/date string in an appropriate format. Presently "YYYY-mm-dd HH:MM:SS"
* ``log(message,severity=SOLE.LOG_NOTICE)`` - this takes the action of logging information. At present this logs everything to console.
* ``new_id(class="UnspecifiedClass")`` - returns a unique ID for the specific object of type class

These functions can be overridden if desired. For example, to make SOLE use UUID's for the base object id's:

```
import uuid
def new_id(baseclass='UnspecifiedClass'):
    return uuid.uuid4()
```

Which then results in ids like "4d9c4052-c83e-4ee7-b7c4-4b0b86a6db77" as opposed to "BF-00001"

SOLE also provides a number of variables and constants to support simulator operations:

| Attribute | Description |
| --------- | ----------- |
| ``current_tick`` | positive integer, indicating what unit of time we are currently on |
| ``tick_ratio_to_real_time`` | positive float, indicating ratio of tick to real world seconds |
| ``LOG_DEBUG`` | constant integer, used for indicating log severity |
| ``LOG_INFO`` | constant integer, used for indicating log severity |
| ``LOG_NOTICE`` | constant integer, used for indicating log severity |
| ``LOG_WARNING`` | constant integer, used for indicating log severity |
| ``LOG_ERR`` | constant integer, used for indicating log severity |
| ``LOG_CRIT`` | constant integer, used for indicating log severity |
| ``LOG_ALERT`` | constant integer, used for indicating log severity |
| ``LOG_EMERG`` | constant integer, used for indicating log severity |
| ``verbosity`` | integer, the current level of log output which is an OR'd combination of the log levels |


