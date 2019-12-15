from math import gcd

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

class UnitVector(Vector):
	def __init__(self, **args):
		if "vec" in args:
			factor = gcd(args["vec"].x, args["vec"].y)
			self.x = args["vec"].x / factor
			self.y = args["vec"].y / factor
		elif "x" in args and "y" in args:
			factor = gcd(args["x"], args["y"])
			self.x = args["x"] / factor
			self.y = args["y"] / factor
		else:
			raise ValueError("Unit Vector parameter error")
	
	def __add__(self, vec):
		return UnitVector(x = self.x + vec.x, y = self.y + vec.y)
	
	def __sub__(self, vec):
		return UnitVector(x = self.x - vec.x, y = self.y - vec.y)

def get_string(file_name):
	with open(file_name, "r") as input_file:
		return input_file.read()

def get_meteors(file_name):
	meteors = []
	lines = get_string(file_name).split("\n")
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == "#":
				meteors.append(Vector(i,j))
	return meteors

def compile_los(meteors, position):
	los = []
	for meteor in meteors:
		if meteor == position:
			pass
		else:
			relative = UnitVector(vec = meteor - position)
			if relative in los:
				pass
			else:
				los.append(relative)
	return len(los)

def iterate_meteors(file_name):
	meteors = get_meteors(file_name)
	largest = (0,None)
	for meteor in meteors:
		seen = compile_los(meteors, meteor)
		if seen > largest[0]:
			largest = (seen,meteor)
	return largest

print(iterate_meteors("day10_input.txt"))