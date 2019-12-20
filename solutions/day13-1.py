from aoc_opcode import Opcode
from vector import Vector

def create_map():
	map = [[0] * 27 for x in range(37)]
	
	opc = Opcode("day13_input.txt")
	output = [opc.get_next(), opc.get_next(), opc.get_next()]
	while output != [None, None, None]:
		map[output[0]][output[1]] = output[2]
		output = [opc.get_next(), opc.get_next(), opc.get_next()]
	
	return map

level = create_map()
count = 0
for y in range(27):
	for x in range(37):
		tile = level[x][y]
		if tile == 0:
			print(' ', end = '')
		elif tile == 1:
			print('#', end = '')
		elif tile == 2:
			count += 1
			print('=', end = '')
		elif tile == 3:
			print('-', end = '')
		elif tile == 4:
			print('o', end = '')
	print()
print(count)