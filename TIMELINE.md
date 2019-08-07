Variables
----------
Floor height: 2.5 m / floor
Elevator movement rate: 1 m / tick
Wait at floor: 10 ticks
Current floor

Timeline reference
-------------------
Assuming real time may be a large multiple of ticks, ticks are kept unmultiplied for simplicity.

Time | Velocity	| Elevation | Status | Current Floor | People aboard
---- | -------- | --------- | ------ | ------------- | -------------
0 ticks |  +0 m / t |  0 m |  About to go to floor 2  |  Lobby  |  None
1 ticks |  +1 m / t |  1 m  | Going to floor 2  |  None  |  None
2 ticks |  +1 m / t |  2 m  | Going to floor 2  |  None  |  None
3 ticks |  +1 m / t |  3 m | Going to floor 2  |  None  | None
4 ticks |  +1 m / t |  4 m | Going to floor 2  |  None  | None
5 ticks |  0 m / t |  5 m  | At floor 2  |  Floor 2  |  None
6 ticks |  0 m / t |  5 m  | People entering  |  Floor 2  |  +x people
7 ticks |  0 m / t |  5 m  | About to go to floor 1  |  Floor 2  | x people
8 ticks |  1 m / t |  4 m  | Going to floor 1  |  None  |  x people
9 ticks |  1 m / t |  3 m  | Going to floor 1  |  None  |  x people
10 ticks | 0 m / t |  2.5 m  | At floor 1  |  Floor 1  |  x people
11 ticks | 0 m / t |  2.5 m  | People exiting  | Floor 1  | -x people
12 ticks | 0 m / t |  2.5 m  | Standing by  | Floor 1  |  None

Pseudocode
----------

class elevator:	
	
	# Variables
	int floorHeight
	int moveRate
	int posY
	int currentFloor	
	int targetFloor
	

	# Methods - Called once per tick
	
	ChangePosition(rate):
		# Elevator's position must be changed by referencing movement rate.
		# +1 = up by 1 m / tick
		# 0 = stationary
		# -1 = down by 1 m / tick
		posY += rate
		
	ReturnCurrentFloor():
		return currentFloor

	MonitorCurrentFloor(FloorObject, targetFloor):
		# As each floor has a static height in space, compare to elevator's height.
		# Change currentFloor if posY equals or exceeds floor.
		if posY => FloorObject.height:
			currentFloor = FloorObject.id
		else return None
	
		# To reach target floor, elevator must wait, because velocity is integer.
		# if abs value of diff in height <= 1 AND abs value diff currentFloor and target <= 1
		# Then elevator is about to reach/exceed the height of target and must stop
		if ([targetFloor.height - posY] <= 1) AND ([currentFloor - targetFloor] <= 1):
			# Stop elevator when destination reached
			rate = 0
			posY = FloorObject.height	
		
				
