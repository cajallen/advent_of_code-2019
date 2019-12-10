import timeit

mycode = """
planets = {
	"MAIN": {
		#sub planets are ALL subplanets
		"dir": [],
		#direct planets are only direct subplanets
		"sub": []
	}
}

def add_planet(alpha, beta):
	# if beta is already in the tree
	if beta in planets["MAIN"]["sub"]:
		current = "MAIN"
		# loop through until beta is a direct child of current (this should only occur once in the tree)
		while (beta not in planets[current]["dir"]):
			for child in planets[current]["dir"]:
				if beta in planets[child]["sub"]:
					current = child
					# remove beta and it's subtrees from subtrees on the way
					planets[current]["sub"].remove(beta)
					planets[current]["sub"].remove(planets[beta]["sub"])
		# then remove it
		planets[current]["dir"].remove(beta)
	# else just add it to main's subs
	else:
		planets[beta] = {
			"dir": [],
			"sub": []
		}
		planets["MAIN"]["sub"].append(beta)
	
	# if alpha is already in the tree
	if alpha in planets["MAIN"]["sub"]:
		current = "MAIN"
		# loop through it until we arrive at alpha
		while (alpha != current):
			for child in planets[current]["dir"]:
				if alpha in planets[child]["sub"] or child == alpha:
					# add beta and it's subtree to the subtrees on the way
					current = child
					planets[current]["sub"] += (planets[beta]["sub"] + [beta])
		planets[current]["dir"].append(beta)


	# if it's not, just add alpha to MAIN's subtree and add beta in the normal way
	else:
		planets["MAIN"]["sub"].append(alpha)
		planets["MAIN"]["dir"].append(alpha)
		planets[alpha] = {
			"dir": [beta],
			"sub": planets[beta]["sub"] + [beta]
		}

#handles text file input
def write_planets(file_name):
	with open(file_name, "r") as input_file:
		rl = input_file.readline()
		while rl != "":
			rl = rl.split(")")
			add_planet(rl[0].strip(), rl[1].strip())
			rl = input_file.readline()

def find_path_to_orbitee_of(planet):
	path = []
	current = "MAIN"
	while planet not in planets[current]["dir"]:
		for child in planets[current]["dir"]:
			if planet in planets[child]["sub"] or planet == child:
				current = child
				break
		path.append(current)
	return path

def find_path_between(planet1, planet2):
	write_planets("day6_input.txt")
	path_to_you = find_path_to_orbitee_of(planet1) 
	path_to_santa = find_path_to_orbitee_of(planet2)

	total = 0
	for i in range(len(path_to_you)):
		if path_to_you[i] != path_to_santa[i % len(path_to_santa)]:
			total += 1
	for i in range(len(path_to_santa)):
		if path_to_you[i % len(path_to_you)] != path_to_santa[i]:
			total += 1
	return total

find_path_between("YOU", "SAN")"""

print (timeit.timeit(stmt = mycode, number = 100))