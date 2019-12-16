from math import gcd
from time import perf_counter
from copy import deepcopy


def get_string(file_name):
	with open(file_name, "r") as input_file:
		return input_file.read()

def get_meteors(file_name):
	meteors = []
	lines = get_string(file_name).split("\n")
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == "#":
				meteors.append((i,j))
	return meteors

def print_map(map):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j]:
				print('#', end = '')
			else:
				print(' ', end = '')
		print('')

temp = get_meteors("day10_input.txt")
map = [[False] * 34 for x in range(34)]
for coord in temp:
	map[coord[0]][coord[1]] = True

t1 = perf_counter()

test = [item for item in map]
count = 0
for i in range(34):
	for j in range(34):
		collided = False
		if i == j == 0:
			pass
		else:
			x = i
			y = j
			while x < 34 and y < 34:
				if collided:
					test[x][y] = False
				else:
					if test[x][y]:
						collided = True
						test[x][y] = False
						count += 1
				x += i
				y += j
print(count)

print(416*(perf_counter() - t1))