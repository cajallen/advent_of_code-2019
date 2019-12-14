def get_opcode(file_name):
	with open(file_name, "r") as input_file:
		input_string = input_file.read()
		return list(map(int, input_string.split(",")))


def set_element(list, position, element):
	while len(list) < position + 1:
		list.append(0)
	list[position] = element

def get_element(list, position):
	if position > len(list) - 1:
		return 0
	return list[position]

def get_position(opcode, i, operation, mode, position, offset):
	# literal mode: 
	if (position == "3" and operation not in []) or (position == "1" and operation in ["3"]):
		if mode in ["0", "1"]:
			return i + position
		return i + position + offset
		
	if mode == "0":
		return get_element(opcode, i + position)
	if mode == "1":
		return i + position
	if mode == "2":
		return get_element(opcode, i + position) + offset
	

def iterate_opcode(opcode, input_queue=[]):
	# opcode position
	i = 0
	offset = 0

	while True:
		full_operation = str(get_element(opcode, i)).rjust(5, '0')
		operation = full_operation[3:5]


		# end
		if operation == "99":
			yield None

		pos1 = get_position(opcode, i, operation, full_operation[2], 1, offset)
		
		if operation not in ["03", "04", "09"]:
			pos2 = get_position(opcode, i, operation, full_operation[1], 2, offset)
		
			if operation not in ["05", "06"]:
				pos3 = get_position(opcode, i, operation, full_operation[0], 3, offset)

		# add
		if operation == "01":
			set_element(opcode, pos3, get_element(opcode, pos1) + get_element(opcode, pos2))

			if str(get_element(opcode, i)).rjust(5, '0') == full_operation:
				i += 4

		# mult
		elif operation == "02":
			set_element(opcode, pos3, get_element(opcode, pos1) * get_element(opcode, pos2))

			if str(get_element(opcode, i)).rjust(5, '0') == full_operation:
				i += 4

		# input
		elif operation == "03":
			if len(input_queue) > 0:
				set_element(opcode, pos1, input_queue.pop(0))
			else:
				set_element(opcode, pos1, int(input("input: ")))

			if str(get_element(opcode, i)).rjust(5, '0') == full_operation:
				i += 2

		# output
		elif operation == "04":
			yield get_element(opcode, pos1)
			i += 2

		# jump if !0
		elif operation == "05":
			if get_element(opcode, pos1) != 0:
				i = get_element(opcode, pos2)
			else:
				i += 3

		# jump if 0
		elif operation == "06":
			if get_element(opcode, pos1) == 0:
				i = get_element(opcode, pos2)
			else:
				i += 3

		# less than
		elif operation == "07":
			if get_element(opcode, pos1) < get_element(opcode, pos2):
				set_element(opcode, pos3, 1)
			else:
				set_element(opcode, pos3, 0)

			if str(get_element(opcode, i)).rjust(5, '0') == full_operation:
				i += 4

		# equals
		elif operation == "08":
			if get_element(opcode, pos1) == get_element(opcode, pos2):
				set_element(opcode, pos3, 1)
			else:
				set_element(opcode, pos3, 0)

			if str(get_element(opcode, i)).rjust(5, '0') == full_operation:
				i += 4
		
		# offset adjustment
		elif operation == "09":
			offset += get_element(opcode, pos1)

			i += 2
		
		# oopsie
		else:
			print(full_operation, i, offset)
			break

def run_opcode(file_name):
	opcode = get_opcode(file_name)
	gen = iterate_opcode(opcode, [2])
	output = [next(gen)]
	while output[-1] != None:
		output.append(next(gen))
	print(output)

run_opcode("day9_input.txt")