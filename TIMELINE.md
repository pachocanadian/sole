vvv To be moved to appropriate documentation vvv

## Basic Elevator Behaviour Outline
------------
A SOLE elevator behaves as follows:

A person on floor x requests an elevator so they can move to floor y. 
Receiving a request causes an elevator to start moving to floor x to pick up the person.
The elevator reaches floor x and stops, allowing the person to get onto it.
The elevator moves the person to floor y and stops, allowing the person to get off.

Additional requests are ignored until the elevator completes the first request it receieves. 

### Basic Elevator Example Scenario
------------
Assuming one elevator idle at Lobby:

1) Person A at floor 2 requests an elevator to move them to floor 1.
2) Elevator at Lobby receives request and begins to move to floor 2
3) Elevator reaches floor 2, stops, and picks up person.
4) Person B requests an elevator to move Person B to Lobby [Request is ignored].
5) Elevator (person A onboard) begins moving to floor 1.
6) Elevator (person A onboard) reaches floor 1 and stops, letting person A off.
7) Elevator is now idle and can repeat step 1 for a new request.


### Basic Elevator Timeline and Ruleset 
-------------------
* Boarding an elevator takes 5 seconds.
* Leaving an elevator takes 5 seconds.
* Elevator prepares for 1 second in an "about to do x" state before doing x.
* Acceleration is instantaneous
* Elevator base velocity units are +1 m/s, 0 m/s or -1 m/s.

Time (sec)   | Velocity	 | Elevation | Status                  | Current Floor | People aboard
------------ | --------  | --------- | --------------------    | ------------- | -------------
0            |  +0 m / s |  0 m      | Idle                    |  Lobby        |  None
1	     |  +0 m / s |  0 m      | About to go to floor 2  |  Lobby        |
2            |  +1 m / s |  1 m      | Going to floor 2        |  None         |  None
3            |  +1 m / s |  2 m      | Going to floor 2	       |  None         |  None
4            |  +1 m / s |  3 m      | Going to floor 2        |  None         |  None
5            |  +1 m / s |  4 m      | Going to floor 2        |  None         |  None
6            |  0 m / s  |  5 m      | At floor 2              |  Floor 2      |  None
7 - 11       |  0 m / s  |  5 m      | People entering         |  Floor 2      | +x people
12           |  0 m / s  |  5 m      | About to go to floor 1  |  Floor 2      |  x people
13           |  1 m / s  |  4 m      | Going to floor 1        |  None         |  x people
14           |  1 m / s  |  3 m      | Going to floor 1        |  None         |  x people
15           |  0 m / s  |  2.5 m    | At floor 1              |  Floor 1      |  x people
16 - 21      |  0 m / s  |  2.5 m    | People exiting          |  Floor 1      | -x people
22           |  0 m / s  |  2.5 m    | Idle	               |  Floor 1      |  None


## Building Layout

Floor height: 2.5 m / floor

Elevation	|	Floor		|	
---------------	|	-------		|
10		|	Floor 4		|
7.5		|	Floor 3 	|	
5		|	Floor 2 	|
2.5		|	Floor 1		|
0		|	Lobby		|



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
