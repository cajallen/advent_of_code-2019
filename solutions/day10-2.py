from math import floor
from vector import Vector


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
	map = [[False] * 34 for x in range(34)]
	for meteor in meteor_list:
		map[meteor.y][meteor.x] = True
	return map

# function to visualize the meteor field
def print_map(map, pos=None):
	for y in range(len(map)):
		for x in range(len(map[y])):
			if pos is not None and pos == Vector(x, y):
				print('@', end=' ')
			elif map[y][x] == False:
				print(' ', end=' ')
			elif map[y][x] == 200:
				print('x', end = ' ')
			else:
				print('o', end=' ')
		print('')

# returns the farey sequence (simplified vector pairs in rotational sequence) from 0,1 to 1,0
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


def laser_quadrant(meteor_map, quad, pos, count):
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
	for vec in vectors:
		x = pos.x + vec.x
		y = pos.y + vec.y

		while -1 < x < len(meteor_map[0]) and -1 < y < len(meteor_map):
			if meteor_map[y][x]:
				if count == 200:
					print(Vector(x,y))
				meteor_map[y][x] = count
				count += 1
				break
			x += vec.x
			y += vec.y
	return count
	

def iterate_laser(file_name, pos):
	meteor_list = get_meteor_list(file_name)
	meteor_map = get_map(meteor_list)
	count = 1
	while count < 200:
		for i in range(1, 5):
			count = laser_quadrant(meteor_map, i, pos, count)
	print_map(meteor_map, pos)


iterate_laser("day10_input.txt", Vector(23,20))