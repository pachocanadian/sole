Variables
----------
Floor height: 2.5 m / floor
Elevator movement rate: 1 m / tick
Wait at floor: 10 ticks
Current floor
People aboard


Assumptions
------------
Elevator commits to moving to the first floor it is instructed to move toward unless it receives a request to move to another floor that is between its current position and the target floor. Additional move instructions must then be queued up to a limit (initially 3, for simplicity).

Assuming elevator start position of lobby:
1) Elevator receives request to move to floor 2
2) Elevator begins moving to floor 2.
3) Elevator receives new request to move to floor 1
4) Elevator must now stop at floor 1, before then moving to floor 2.
5) If elevator receives a move request (e.g. "move to floor 3") that is not in between lobby and floor 2, AND elevator has not reached floor 2, elevator will prioritize movement between lobby and floor 2 and add the request to move to floor 3 to an array of pending move instructions.
6) Additional movement requests after that point that fit the definition of (5) are stacked into a list of pending movements, up to a limit of 2 in addition to the first movement (total 3). 

Timeline reference (needs additional fleshing out to account for new assuptions)
-------------------
Assuming real time may be a large multiple of ticks, ticks are kept unmultiplied for simplicity.

Time (ticks) | Velocity	| Elevation | Status | Current Floor | People aboard
---- | -------- | --------- | ------ | ------------- | -------------
0 |  +0 m / t |  0 m |  About to go to floor 2  |  Lobby  |  None
1 |  +1 m / t |  1 m  | Going to floor 2  |  None  |  None
2 |  +1 m / t |  2 m  | Going to floor 2  |  None  |  None
3 |  +1 m / t |  3 m | Going to floor 2  |  None  | None
4 |  +1 m / t |  4 m | Going to floor 2  |  None  | None
5 |  0 m / t |  5 m  | At floor 2  |  Floor 2  |  None
6 |  0 m / t |  5 m  | People entering  |  Floor 2  |  +x people
7 |  0 m / t |  5 m  | About to go to floor 1  |  Floor 2  | x people
8 |  1 m / t |  4 m  | Going to floor 1  |  None  |  x people
9 |  1 m / t |  3 m  | Going to floor 1  |  None  |  x people
10 | 0 m / t |  2.5 m  | At floor 1  |  Floor 1  |  x people
11 | 0 m / t |  2.5 m  | People exiting  | Floor 1  | -x people
12 | 0 m / t |  2.5 m  | Standing by  | Floor 1  |  None

Pseudocode (incomplete)
* Below is not yet clean and not representative of finalized algorithm, including comment syle/verbage...
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
		for floor in Basebuilding.floors:
			if posY == building.elevationAt(floor):
				currentFloor = floor.id
		else return None
	
		# To reach target floor, elevator must wait, because velocity is integer.
		# if absolute value abs() of difference in height <= 1 AND abs(difference between currentFloor and target <= 1)
		# Then elevator is about to reach/exceed the height of target and must stop
		if (abs(elevationAt(targetFloor) - posY) <= 1) AND (posY - elevationAt(targetFloor)] <= 1):
			# Stop elevator when destination reached
			rate = 0
			posY = elevationAt(targetFloor)	
		
		# Check for movement request interrupts... incomplete		
