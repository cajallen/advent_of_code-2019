from aoc_opcode import Opcode
from vector import Vector
from os import system
from math import copysign


def create_map(output):
	for coord in output:
		map[coord[0]][coord[1]] = coord[2]

	return map


def display_level(level, score):
	for y in range(27):
		for x in range(37):
			tile = level[x][y]
			if tile == 0:
				print(' ', end='')
			elif tile == 1:
				print('#', end='')
			elif tile == 2:
				print('=', end='')
			elif tile == 3:
				print('-', end='')
			elif tile == 4:
				print('o', end='')
		print()
	print("score:", score)


def iterate_frames():
	#opcode
	input = []
	opc = Opcode("day13_input.txt", input)

	#game
	score = 0
	map = [[0] * 27 for x in range(37)]

	#ai
	ball = 0
	paddle = 0
	while True:
		output = opc.get_next()
		if output == -2:
			input.append(min(max(ball - paddle, -1), 1))
			#system('cls')
			#display_level(map, score)

		else:
			output = [output, opc.get_next(), opc.get_next()]

			if output[0] == None:
				print(score)
				break

			elif output[0] == -1:
				score = output[2]

			else:
				map[output[0]][output[1]] = output[2]

				if output[2] == 3:
					paddle = output[0]
				if output[2] == 4:
					ball = output[0]


iterate_frames()
