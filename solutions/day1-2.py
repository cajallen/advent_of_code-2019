def get_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
	else:
		return fuel + get_fuel(fuel)

def get_total_fuel(file_name):
    with open(file_name, "r") as input_file:        
        total = 0
        for line in input_file.read().split("\n")
            total += get_fuel(int(line))
        
        return total
    
print(get_total_fuel("day1_input.txt"))