# WIP

def iterate_opcode(opcode, automated_inputs):
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
			print(opcode[pos1])
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

with open("day7_input.txt", "r") as input_file:
	input_string1 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
	input_string = input_file.read()
	opcode = list(map(int, input_string1.split(",")))
	iterate_opcode(opcode, [])