from aoc_opcode import Opcode
from vector import Vector
import matplotlib.pyplot as plt

class Robot:
	def __init__(self):
		self.position = Vector(0,0)
		self.direction = 1

	def __repr__(self):
		if self.direction == 0:
			return str(self.position) + ", right"
		if self.direction == 1:
			return str(self.position) + ", up"
		if self.direction == 2:
			return str(self.position) + ", left"
		if self.direction == 3:
			return str(self.position) + ", down"
		
	def turn(self, change):
		self.direction = (self.direction + change) % 4
		self.position += Vector((self.direction % 2 - 1) * (1 - self.direction), (self.direction % 2) * (2 - self.direction))

def run():
	robert = Robot()

	tiles = { 
		robert.position: 1
	}
	input = []
	opc = Opcode("day11_input.txt", input)

	count = 1
	while True:
		tile = tiles.get(robert.position, None)
		if tile == None:
			count += 1
			tile = 0
		input += [tile]
			
		instructions = (opc.get_next(), opc.get_next())
		if instructions == (None, None):
			break
		tiles[robert.position] = instructions[0]	
		robert.turn(instructions[1] * 2 - 1)

	x = [vec.x for vec in tiles.keys() if tiles[vec] == 1]
	y = [vec.y for vec in tiles.keys() if tiles[vec] == 1]
	
	# idk how the fk to use matplotlib, so just squeeze the window down to see the answer... lol
	plt.plot(x, y, 'go--', linewidth = 0, markersize = 8, marker = 's')
	plt.show()

run()
