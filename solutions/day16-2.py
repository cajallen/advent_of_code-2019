from math import log, ceil
from time import perf_counter


def get_input(file_name):
	with open(file_name, "r") as input_file:
		return [int(s) for s in input_file.read()]

def run(num):
	num = num * 10000
	start_offset = int("".join([str(x) for x in num[0:7]]))
	for _ in range(1, 101):
		s = sum(num[start_offset:])
		for i in range(start_offset, len(num)):
			n = num[i]
			num[i] = abs(s) % 10
			s -= n
	print(num[start_offset : start_offset + 8])

run(get_input("day16_input.txt"))