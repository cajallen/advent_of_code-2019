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