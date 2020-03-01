class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __eq__(self, vec2):
		return self.x == vec2.x and self.y == vec2.y

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"
	
	def __add__(self, vec):
		return Vector(self.x + vec.x, self.y + vec.y)
	
	def __sub__(self, vec):
		return Vector(self.x - vec.x, self.y - vec.y)

	def __hash__(self):
		return hash((self.x, self.y))
	
	def get_h(self, vec):
		between = vec - self
		return abs(between.x) + abs(between.y)

class Vector3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __eq__(self, vec):
		return self.x == vec.x and self.y == vec.y and self.z == vec.z

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
	
	def __add__(self, vec):
		return Vector3(self.x + vec.x, self.y + vec.y, self.z + vec.z)
	
	def __sub__(self, vec):
		return Vector3(self.x - vec.x, self.y - vec.y, self.z - vec.z)

	def __hash__(self):
		return hash((self.x, self.y, self.z))
	
	def compare_position(self, vec):
		x = min(max(vec.x - self.x, -1), 1)
		y = min(max(vec.y - self.y, -1), 1)
		z = min(max(vec.z - self.z, -1), 1)
		return Vector3(x,y,z)
	
	def sum(self):
		return abs(self.x) + abs(self.y) + abs(self.z)