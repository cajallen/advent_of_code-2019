# WIP
def get_opcode(file_name):
	with open(file_name, "r") as input_file:
		input_string = input_file.read()
		return list(map(int, input_string.split(",")))

def iterate_opcode(opcode, automated_inputs = []):
	i = 0
	while(True):
		operation = str(opcode[i]).rjust(5, '0')
		
		#end
		if (operation[-2:] == "99"):
			break
		
		
		pos1 = opcode[i+1] if operation[-3] == "0" else i+1
		#add
		if (operation[-1] == "1"):
			pos2 = opcode[i+2] if operation[-4] == "0" else i+2
			pos3 = opcode[i+3] if operation[-5] == "0" else i+3
			opcode[pos3] = opcode[pos1] + opcode[pos2]

			if (str(opcode[i]).rjust(5, '0') == operation):
				i += 4

		#mult
		elif (operation[-1] == "2"):
			pos2 = opcode[i+2] if operation[-4] == "0" else i+2
			pos3 = opcode[i+3] if operation[-5] == "0" else i+3
			opcode[pos3] = opcode[pos1] * opcode[pos2]

			if (str(opcode[i]).rjust(5, '0') == operation):
				i += 4

		#input
		elif (operation[-1] == "3"):
			if len(automated_inputs) > 0:
				opcode[pos1] = automated_inputs.pop(0)
			else:
				opcode[pos1] = int(input("input: "))

			if (str(opcode[i]).rjust(5, '0') == operation):
				i += 2

		#output
		elif (operation[-1] == "4"):
			return opcode[pos1]
			i += 2

		#jump if !0
		elif (operation[-1] == "5"):
			if(opcode[pos1] != 0):
				pos2 = opcode[i+2] if operation[-4] == "0" else i+2
				i = opcode[pos2]
			else:
				i += 3

		#jump if 0
		elif (operation[-1] == "6"):
			if(opcode[pos1] == 0):
				pos2 = opcode[i+2] if operation[-4] == "0" else i+2
				i = opcode[pos2]
			else:
				i += 3

		#less than
		elif (operation[-1] == "7"):
			pos2 = opcode[i+2] if operation[-4] == "0" else i+2
			pos3 = opcode[i+3] if operation[-5] == "0" else i+3
			if (opcode[pos1] < opcode[pos2]):
				opcode[pos3] = 1
			else:
				opcode[pos3] = 0

			if (str(opcode[i]).rjust(5, '0') == operation):
				i += 4

		#equals
		elif (operation[-1] == "8"):
			pos2 = opcode[i+2] if operation[-4] == "0" else i+2
			pos3 = opcode[i+3] if operation[-5] == "0" else i+3
			if (opcode[pos1] == opcode[pos2]):
				opcode[pos3] = 1
			else:
				opcode[pos3] = 0

			if (str(opcode[i]).rjust(5, '0') == operation):
				i += 4

		else:
			print(opcode)
			break

def run_thruster_sequence(opcode, phases):
	initial_value = 0
	for phase in phases:
		initial_value = iterate_opcode(opcode, [phase, initial_value])
	return initial_value

def iterate_thruster_sequences(opcode):
	highest = [0, [0, 0, 0, 0, 0]]
	for x1 in range(5):
		for x2 in range(4):
			for x3 in range(3):
				for x4 in range(2):
					nums = list(range(5))
					output = run_thruster_sequence(opcode, [nums.pop(x1), nums.pop(x2), nums.pop(x3), nums.pop(x4), nums[0]])
					if output > highest[0]:
						nums = list(range(5))
						highest = [output, [nums.pop(x1), nums.pop(x2), nums.pop(x3), nums.pop(x4), nums[0]]]
	return highest

print(iterate_thruster_sequences(get_opcode("day7_input.txt")))
