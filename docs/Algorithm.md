
Pseudocode (incomplete)
----------

class elevator:	
	
	# Variables
	int floorHeight
	int moveRate
	int posY
	int currentFloor	
	int Person.targetFloor
	

	# Methods - Called once per tick
	
	ChangePosition(moveRate):
		posY += moveRate
		
	ReturnCurrentFloor():
		return currentFloor

	MonitorCurrentFloor(FloorObject, targetFloor):
		"""Change currently floor if elevator stops at a floor by comparing elevator position to floor elevations."""
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
