# Default attributes for SOLE objects


### SOLE.Building.BaseBuilding

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`_at_elevation`|A mapping of elevations->objects.|{}|
|`_elevation_of`|A mapping of objects->elevations.|{}|
|`_ref_to`|A mapping of ids->objects.|{}|
|`elevators`|The elevators contained in the building.|[]|
|`floors`|The floors contained in the building.|[]|
|`height`|The overall height of the building.|0.0|
|`id`|A unique string identifying the object. Generally not human friendly.||
|`label`|A human friendly descriptor of the object.||


### SOLE.Building.BaseElevator

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`building`|A reference to the current building object the elevator is contained within.|None|
|`carrying`|A list of Person objects presently within the elevator|[]|
|`destination`|The current destination floor that we are moving towards. Set to None when not in motion.|None|
|`elevation`|The elevation of the top-most point of the elevator.|0.0|
|`floor_requests`|A list of floor requests in sequential order.|[]|
|`height`|The height of the elevator itself.|2.44|
|`id`|A unique string identifying the object. Generally not human friendly.||
|`label`|A friendly identifier for the elevator||
|`loading_time_needed`|Real world seconds that it takes to load the elevator.|5.0|
|`maximum_down_speed`|A maximum downward velocity for the elevator, must be <0|-1.0|
|`maximum_up_speed`|A maximum upward velocity for the elevator, must be >0|1.0|
|`status`|The current status of the elevator.|waiting|
|`status_percent`|A float inside [0,1] indicating percentage completion of status.|1.0|
|`unloading_time_needed`|Real world seconds that it takes to unload the elevator.|5.0|
|`velocity`|Positive velocity means upwards, negative means downward, 0 is at rest|0.0|


### SOLE.Building.BaseFloor

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`building`|A reference to the parent building object.|None|
|`carrying`|A list of the people contained within the floor object.|[]|
|`elevation`|The distance of the bottom-most point of the object from the ground.|0.0|
|`elevation_top`|The distance of the top-most point of the object from the ground.|0.0|
|`height`|The height of the floor.|3.0|
|`id`|A unique string identifying the object. Generally not human friendly.||
|`is_floor`|A boolean indicating whether we are a floor object or not.|True|
|`label`|A human friendly descriptor of the object.||


### SOLE.Building.BasePerson

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`building`|A reference to the parent building.|None|
|`destination`|A reference to the floor/elevator that we are destined to.|None|
|`height`|The height of the person.|1.77|
|`id`|A unique string identifying the object. Generally not human friendly.||
|`label`|A human friendly descriptor of the object.|Jonathan|
|`location`|A reference to the object the person is contained in, whether floor or elevator.|None|
|`status`|The current status of the person.|idle|
|`status_percent`|A float inside [0,1] indicating percentage completion of the status.|1.0|
