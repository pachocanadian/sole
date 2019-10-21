# Default attributes for SOLE objects


### SOLE.Building.BaseBuilding

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`id`|A unique string identifying the object. Generally not human friendly.||
|`label`|A human friendly descriptor of the object.||
|`height`|The overall height of the building.|0.0|
|`floors`|The floors contained in the building.|[]|
|`elevators`|The elevators contained in the building.|[]|
|`_elevation_of`|A mapping of objects->elevations.|{}|
|`_at_elevation`|A mapping of elevations->objects.|{}|
|`_ref_to`|A mapping of ids->objects.|{}|


### SOLE.Building.BaseElevator

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`height`|The height of the elevator itself.|2.44|
|`elevation`|The elevation of the top-most point of the elevator.|0.0|
|`destination`|The current destination floor that we are moving towards. Set to None when not in motion.|None|
|`velocity`|Positive velocity means upwards, negative means downward, 0 is at rest|0.0|
|`label`|A friendly identifier for the elevator||
|`maximum_up_speed`|A maximum upward velocity for the elevator, must be >0|1.0|
|`maximum_down_speed`|A maximum downward velocity for the elevator, must be <0|-1.0|
|`carrying`|A list of Person objects presently within the elevator|[]|
|`building`|A reference to the current building object the elevator is contained within.|None|
|`floor_requests`|A list of floor requests in sequential order.|[]|
|`status`|The current status of the elevator.|waiting|
|`status_percent`|A float inside [0,1] indicating percentage completion of status.|1.0|
|`unloading_time_needed`|Real world seconds that it takes to unload the elevator.|5.0|
|`loading_time_needed`|Real world seconds that it takes to load the elevator.|5.0|
|`id`|A unique string identifying the object. Generally not human friendly.||


### SOLE.Building.BaseFloor

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`id`|A unique string identifying the object. Generally not human friendly.||
|`height`|The height of the floor.|3.0|
|`elevation`|The distance of the bottom-most point of the object from the ground.|0.0|
|`elevation_top`|The distance of the top-most point of the object from the ground.|0.0|
|`label`|A human friendly descriptor of the object.||
|`carrying`|A list of the people contained within the floor object.|[]|
|`building`|A reference to the parent building object.|None|
|`is_floor`|A boolean indicating whether we are a floor object or not.|True|


### SOLE.Building.BasePerson

|*Attribute*|*Description*|*Default Value*|
| --- | --- | --- |
|`id`|A unique string identifying the object. Generally not human friendly.||
|`height`|The height of the person.|1.77|
|`location`|A reference to the object the person is contained in, whether floor or elevator.|None|
|`building`|A reference to the parent building.|None|
|`destination`|A reference to the floor/elevator that we are destined to.|None|
|`label`|A human friendly descriptor of the object.|Annika|
