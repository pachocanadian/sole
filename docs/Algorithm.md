
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
	

	# Methods

	def move():
		''' Called once per tick(). '''
		# Get person's requested target floor.
		dest_y = elevation_at(Person.target_floor) # Person object as a move() parameter?
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
		''' Modify elevator's movement rate. In future, modify to make non-integers.'''
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
	
	def set_carrying(people):
		# Setting/checking who the elevator is carrying will need a better implementation than what I have here.
		self.carrying.append(p)

	
	def return_current_floor():
		return current_floor
	
	
