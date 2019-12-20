from vector import Vector3
# tracking moons, simulate motion to avoid them
# each moon has 3 position values, 3 velocity values (each starts at 0)
# each timestep, update velocity of every moon by applying gravity. 
# then update velocity of every moon by applying gravity.
# to apply gravity, consider each pair of moons.

class Moon:
	def __init__(self, vec):
		self.position = vec
		self.velocity = Vector3(0, 0, 0)
	
	def __repr__(self):
		return "(pos: " + str(self.position) + ", vel: " + str(self.velocity) + ")"
	
	def update_velocity(self, planet):
		self.velocity += self.position.compare_position(planet.position)
	
	def update_position(self):
		self.position += self.velocity
	
	def get_pe(self):
		return self.position.sum()
	
	def get_ke(self):
		return self.velocity.sum()
	
	def get_energy(self):
		return self.get_pe() * self.get_ke()

def get_moons():
	moon1 = Moon(Vector3(16, -11, 2))
	moon2 = Moon(Vector3(0, -4, 7))
	moon3 = Moon(Vector3(6, 4, -10))
	moon4 = Moon(Vector3(-3, -2, -4))
	return [moon1, moon2, moon3, moon4]

def update_moons(moons):
	for moon1 in moons:
		for moon2 in moons:
			moon1.update_velocity(moon2)
	for moon in moons:
		moon.update_position()
	return moons

def run_steps(steps):
	moons = get_moons()
	total_energy = 0
	for i in range(steps):
		moons = update_moons(moons)
	for moon in moons:
		total_energy += moon.get_energy()
	print(total_energy)