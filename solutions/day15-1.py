from aoc_opcode import Opcode
from vector import Vector
from astar import find_path, find_tile
from random import randrange
from os import system
from time import sleep


def get_direction(vec):
	if vec == Vector(0,-1):
		return 1
	if vec == Vector(0,1):
		return 2
	if vec == Vector(-1,0):
		return 3
	if vec == Vector(1,0):
		return 4
	return 0

def map_print(map, pos):
	system('cls')
	for y in range(len(map[0])):
		for x in range(len(map)):
			if map[x][y] == -1:
				print('?', end=' ')
			if map[x][y] == 0:
				print('#', end=' ')
			if map[x][y] == 1:
				if pos == Vector(x, y):
					print('o', end=' ')
				else:
					print(' ', end=' ')
			if map[x][y] == 2:
				if pos == Vector(x, y):
					print('@', end=' ')
				else:
					print('0', end=' ')
		print()


def explore(file_name):
	input = [1]
	opc = Opcode(file_name, input)
	
	oxygen = None
	
	pos = Vector(20,20)
	path = [Vector(0,-1)]
	map = []
	unknown = []
	for x in range(39):
		map.append([])
		for y in range(39):
			if x == 20 and y == 20:
				map[x].append(1)
			elif x % 2 == 0 and y % 2 == 0:
				map[x].append(1)
			elif x % 2 == 1 and y % 2 == 1:
				map[x].append(0)
			else:
				map[x].append(-1)
				unknown.append(Vector(x, y))
	
	while True:
		output = opc.get_next()
		
		if len(path) < 1:
			path = find_tile(map, pos)
		
		if path is None:
			map_print(map, pos)
			break
		
		if output in [0, 1, 2]:
			map_print(map, pos)
			if output == 0:
				if map[path[0].x][path[0].y] == -1:
					unknown.remove(Vector(path[0].x, path[0].y))
				map[path[0].x][path[0].y] = 0
				path = []
			else:
				pos = path[0]
				path.pop(0)
				if map[pos.x][pos.y] == -1:
					unknown.remove(Vector(pos.x, pos.y))
				map[pos.x][pos.y] = output
				if output == 2:
					oxygen = Vector(pos.x, pos.y)
					break
		
		elif output == -2:
			if len(input) < 1:
				input.append(get_direction(path[0] - pos))
	print(len(find_path(map, Vector(20, 20), oxygen)))
explore("day15_input.txt")