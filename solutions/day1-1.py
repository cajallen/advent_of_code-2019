# JOKE SOLUTION
#def get_total_fuel(file_name):
#	with open(file_name, "r") as input_file:
#		return sum([int(x) // 3 - 2 for x in input_file.read().split("\n")])
#	
#print(get_total_fuel("day1-1_input.txt"))

# more readable...
def get_total_fuel(file_name):
    with open(file_name, "r") as input_file:
        get_fuel = lambda x: x // 3 - 2
        
        total = 0
        for line in input_file.read().split("\n")
            total += get_fuel(int(line))
        
        return total
    
print(get_total_fuel("day1_input.txt"))