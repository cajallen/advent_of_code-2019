def get_opcode(file_name):
	with open(file_name, "r") as input_file:
		input_string = input_file.read()
		return list(map(int, input_string.split(",")))

class Opcode:
	# int list: opcode
	# int: i
	# int: offset
	# list: input_queue
	# gen: gen
	
	def __init__(self, file_name, input_queue = []):
		self.opcode = get_opcode(file_name)
		self.inputs = input_queue
		self.i = 0
		self.offset = 0
		self.gen = self.opcode_generator()
	
	def set_element(self, position, element):
		while len(self.opcode) < position + 1:
			self.opcode.append(0)
		self.opcode[position] = element
	
	def get_element(self, position):
		if position > len(self.opcode) - 1:
			return 0
		return self.opcode[position]
	
	def get_position(self, operation, position):
		parameter_mode = int(operation[-2 - position])
		parameter_value = self.get_element(self.i + position)

		# write
		if position == 3 or (position == 1 and operation[3:5] in ["03"]):
			if parameter_mode == 0 or parameter_mode == 1:
				return parameter_value
			if parameter_mode == 2:
				return parameter_value + self.offset
		# read
		if parameter_mode == 0:
			return self.get_element(parameter_value)
		if parameter_mode == 1:
			return parameter_value
		if parameter_mode == 2:
			return self.get_element(parameter_value + self.offset)
		
	def opcode_generator(self):
		while True:
			operation = str(self.get_element(self.i)).rjust(5, '0')
			instruction = operation[3:5]
	
			# end
			if instruction == "99":
				break
	
			pos1 = self.get_position(operation, 1)
			
			if instruction not in ["03", "04", "09"]:
				pos2 = self.get_position(operation, 2)
			
				if instruction not in ["05", "06"]:
					pos3 = self.get_position(operation, 3)
	
			# add
			if instruction == "01":
				self.set_element(pos3, pos1 + pos2)
	
				if str(self.get_element(self.i)).rjust(5, '0') == operation:
					self.i += 4
	
			# mult
			elif instruction == "02":
				self.set_element(pos3, pos1 * pos2)
	
				if str(self.get_element(self.i)).rjust(5, '0') == operation:
					self.i += 4
	
			# input
			elif instruction == "03":
				yield -2
				if len(self.inputs) > 0:
					self.set_element(pos1, self.inputs.pop(0))
				else:
					self.set_element(pos1, int(input("input: ")))
	
				if str(self.get_element(self.i)).rjust(5, '0') == operation:
					self.i += 2
	
			# output
			elif instruction == "04":
				yield pos1
				self.i += 2
	
			# jump if !0
			elif instruction == "05":
				if pos1 != 0:
					self.i = pos2
				else:
					self.i += 3
	
			# jump if 0
			elif instruction == "06":
				if pos1 == 0:
					self.i = pos2
				else:
					self.i += 3
	
			# less than
			elif instruction == "07":
				if pos1 < pos2:
					self.set_element(pos3, 1)
				else:
					self.set_element(pos3, 0)
	
				if str(self.get_element(self.i)).rjust(5, '0') == operation:
					self.i += 4
	
			# equals
			elif instruction == "08":
				if pos1 == pos2:
					self.set_element(pos3, 1)
				else:
					self.set_element(pos3, 0)
	
				if str(self.get_element(self.i)).rjust(5, '0') == operation:
					self.i += 4
			
			# offset adjustment
			elif instruction == "09":
				self.offset += pos1
	
				self.i += 2
			
			# oopsie
			else:
				print(self)
				break
		while True:
			yield None
	
	def get_next(self):
		return next(self.gen)

if __name__ == "__main__":
	opc = Opcode("day11_input.txt", [0])
	output = opc.get_next()
	while output != None:
		print(output)
		output = opc.get_next()