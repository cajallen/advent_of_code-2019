from math import log, ceil
from time import perf_counter


def get_input(file_name):
	with open(file_name, "r") as input_file:
		return [int(s) for s in input_file.read()]

def calculate_row(num, row):
	sum = 0
	for i in range(len(num)):
		if ((i+1)//(row+1)) % 4 == 1:
			sum += num[i]
		elif ((i+1)//(row+1)) % 4 == 3:
			sum -= num[i]
	return abs(sum) % 10

def calculate_phase(num):
	for i in range(len(num)):
		num[i] = calculate_row(num, i)

def iterate_phases(num, phases):
	for _ in range(phases):
		calculate_phase(num)
	return num

t1 = perf_counter()
print(iterate_phases(get_input("day16_input.txt"), 100))
print(perf_counter() - t1)