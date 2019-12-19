from math import floor
from vector import Vector

# this solution uses the farey sequence to generate directions in O(n) time, there is slight waste given that it generates a square of vectors for a rectangular area. 
# the farey sequence generates the fractions from 0 to 1 in order of size, for example for n = 3, it would be 0/1 -> 1/3 -> 1/2 -> 2/3 -> 1/1
# these fractions can be used as vectors, where the direction is arctan of the fraction (not that we need that). funnily enough, we count planets in almost the same exact
# way as we destroy them. 

def get_string(file_name):
	with open(file_name, "r") as input_file:
		return input_file.read()


def get_meteor_list(file_name):
	meteor_list = []
	lines = get_string(file_name).split("\n")
	for line in range(len(lines)):
		for char in range(len(lines[line])):
			if lines[line][char] == "#":
				meteor_list.append(Vector(char, line))
	return meteor_list


def get_map(meteor_list):
	# magic numbers, i do not like but idk how to fix
	map = [[0] * 34 for x in range(34)]
	for meteor in meteor_list:
		map[meteor.y][meteor.x] = 1
	return map

# function to visualize the meteor field
def print_map(map, pos=None):
	for y in range(len(map)):
		for x in range(len(map[y])):
			if pos is not None and pos == Vector(x, y):
				print('@', end=' ')
			elif map[y][x] == 0:
				print(" ", end=' ')
			elif map[y][x] == 1:
				print("o", end=' ')
			elif map[y][x] == 2:
				print("+", end=' ')
			elif map[y][x] == 3:
				print("#", end=' ')
		print('')

def write_farey(meteor_map, pos):
	map = [x for x in meteor_map]
	for i in range(1, 5):
		farey_size = 0
		if i == 1:
			farey_size = max(len(map[0]) - pos.x, pos.y, 1)
		if i == 2:
			farey_size = max(len(map[0]) - pos.x, len(map) - pos.y, 1)
		if i == 3:
			farey_size = max(pos.x, len(map) - pos.y, 1)
		if i == 4:
			farey_size = max(pos.x, pos.y, 1)

		farey = get_vectors(farey_size, i)
		for dir in farey:
			x = pos.x + dir.x
			y = pos.y + dir.y
			if -1 < x < len(map[0]) and -1 < y < len(map):
				map[y][x] += 2
	return map

# returns the farey sequence (simplified vectors in rotational sequence) from 0,1 to 1,0
def get_farey(n):
	x = 0
	y = 0
	x1 = 0
	y1 = 1
	x2 = 1
	y2 = n

	vectors = [Vector(0, 1), Vector(1, n)]
	while y != 1.0:
		x = floor((y1 + n) / y2) * x2 - x1
		y = floor((y1 + n) / y2) * y2 - y1
		x1 = x2
		x2 = x
		y1 = y2
		y2 = y

		vectors += [Vector(x, y)]
	return vectors + [Vector(vec.y, vec.x) for vec in vectors[-2:0:-1]]

# rotates the farey sequence depending on which quadrant we want. this will always go clockwise.
def get_vectors(n, quad):
	quads = [Vector(1, -1), Vector(1, 1), Vector(-1, 1), Vector(-1, -1)]
	xsine = quads[quad - 1].x
	ysine = quads[quad - 1].y
	farey = get_farey(n)

	if quad in [1, 3]:
		return [Vector(xsine * vec.x, ysine * vec.y) for vec in farey]
	elif quad in [2, 4]:
		return [Vector(xsine * vec.y, ysine * vec.x) for vec in farey]


# edits the 1st input
def count_los_quadrant(meteor_map, quad, pos):
	farey_size = 0
	if quad == 1:
		farey_size = max(len(meteor_map[0]) - pos.x, pos.y, 1)
	if quad == 2:
		farey_size = max(len(meteor_map[0]) - pos.x, len(meteor_map) - pos.y, 1)
	if quad == 3:
		farey_size = max(pos.x, len(meteor_map) - pos.y, 1)
	if quad == 4:
		farey_size = max(pos.x, pos.y, 1)

	vectors = get_vectors(farey_size, quad)
	count = 0
	for vec in vectors:
		x = pos.x + vec.x
		y = pos.y + vec.y

		while -1 < x < len(meteor_map[0]) and -1 < y < len(meteor_map):
			if meteor_map[y][x] == 1:
				count += 1
				break
			x += vec.x
			y += vec.y
	return count


def count_los(meteor_map, meteor):
	count = 0
	for i in range(1, 5):
		count += count_los_quadrant(meteor_map, i, meteor)
	return count


def iterate_meteors(file_name):
	meteor_list = get_meteor_list(file_name)
	meteor_map = get_map(meteor_list)
	largest = (0, None)
	for meteor in meteor_list:
		in_los = count_los(meteor_map, meteor)
		if in_los > largest[0]:
			largest = (in_los, meteor)
	print_map(write_farey(meteor_map, largest[1]))
	return largest


print(iterate_meteors("day10_input.txt"))