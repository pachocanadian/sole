
Pseudocode (incomplete)
----------

class elevator:		

	# Variables
	float floor_height
	float velocity
	float pos_y
	float dest_y
	string current_floor	
	string Person.target_floor
	list carrying # Correct data type? Could be better-named variable.	


	# Public methods
	
	def set_carrying(self, p):
		self.carrying = p

	def get_carring(self):
		return self.carrying

	def get_current_floor(self):
		return self.current_floor
	
	
	def move():
		''' Called once per tick(). '''
		# Get Elevator's next target floor.
		dest_y = elevation_at(Elevator.destination_floor)  
		pos_y = elevator.pos_y

		if (dest_y - pos_y) > self.pos_y:
			# Target floor is above elevator.
			change_velocity(1)

		elif (dest_y - pos_y) < self.pos_y
			# Target floor is below elevator.
			change_velocity(-1)

		else: 
			# Elevator has reached target floor.
			change_velocity(0)
			elevator.pos_y = dest_y


	def change_velocity(r):
		''' Modify elevator's movement rate.'''
		if r > 0:
			velocity = maximum_up_speed
		 
		elif r < 0:
			velocity = maximum_down_speed

		else:
			velocity = 0
	
	
	def set_status():
		# Could be more elegant, may need expansion for more statuses.
		if velocity > 1:
			self.status = "Going up."
		
		elif velocity < 1:
			self.status = "Going down."

		else:
			self.status = "Stationary."			
	
	
