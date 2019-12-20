from vector import Vector3
from math import gcd

class Moon1:
	def __init__(self, pos):
		self.position = pos
		self.velocity = 0
	
	def __repr__(self):
		return "(pos: " + str(self.position) + ", vel: " + str(self.velocity) + ")"
	
	def __eq__(self, moon):
		return self.position == moon.position
	
	def update_velocity(self, planet):
		self.velocity += min(max(planet.position - self.position, -1), 1)
	
	def update_position(self):
		self.position += self.velocity

def get_moons():
	moon1 = [16, -11, 2]
	moon2 = [0, -4, 7]
	moon3 = [6, 4, -10]
	moon4 = [-3, -2, -4]
	return [moon1, moon2, moon3, moon4]

def update_moons(moons):
	for moon1 in moons:
		for moon2 in moons:
			moon1.update_velocity(moon2)
	for moon in moons:
		moon.update_position()
	return moons

def check_0_velocity(moons):
	for moon in moons:
		if moon.velocity != 0:
			return False
	return True

def run_iteration():
	cycles = []
	for i in range(3): # 3 dimensions
		moons = [Moon1(x[i]) for x in get_moons()]
		
		count = 0
		while True:
			count += 1
			update_moons(moons)
			if check_0_velocity(moons):
				cycles.append(count)
				break
	return int((cycles[0] * cycles[1] * cycles[2])/gcd(cycles[0], gcd(cycles[1], cycles[2])))

print(run_iteration())