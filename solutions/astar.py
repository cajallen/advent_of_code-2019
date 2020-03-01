from vector import Vector

def find_lowest_f(dict):
	lowest_key = None
	lowest_value = None
	for key in dict:
		if lowest_key is None:
			lowest_key = key
			lowest_value = dict[lowest_key]["h"] + dict[lowest_key]["g"]
		elif dict[lowest_key]["h"] + dict[lowest_key]["g"] < lowest_value:
			lowest_key = key
			lowest_value = dict[lowest_key]["h"] + dict[lowest_key]["g"]
	return lowest_key

def find_lowest_g(dict):
	lowest_key = None
	lowest_value = None
	for key in dict:
		if lowest_key is None:
			lowest_key = key
			lowest_value = dict[lowest_key]["g"]
		elif dict[lowest_key]["g"] < lowest_value:
			lowest_key = key
			lowest_value = dict[lowest_key]["g"]
	return lowest_key

def check_unreachable(map, tile):
	for neighbor in [Vector(0,1), Vector(1,0), Vector(0,-1), Vector(-1,0)]:
		neighbor = neighbor + tile
		if neighbor.x < 0 or len(map) <= neighbor.x or neighbor.y < 0 or len(map[0]) <= neighbor.y:
			pass
		elif map[neighbor.x][neighbor.y] != 0:
			return False
	map[tile.x][tile.y] = 0
	return True

def find_path(map, start, finish, explorative = False): #a* implementation :)
	if check_unreachable(map, finish):
		return None

	non_navi = [0] if explorative else [-1, 0]
	open_nodes = {
		start: {
			"g": 0,
			"h": start.get_h(finish),
			"parent": None
		}
	}
	closed_nodes = {}
	
	while True:
		# no path found, 
		if len(open_nodes) == 0:
			return None
		
		current = find_lowest_f(open_nodes)
		closed_nodes[current] = open_nodes[current]
		del open_nodes[current]
		
		if current == finish:
			path = []
			while closed_nodes[current]["parent"] is not None:
				path.insert(0, current)
				current = closed_nodes[current]["parent"]
			return path
		
		for neighbor in [Vector(0,1), Vector(1,0), Vector(0,-1), Vector(-1,0)]:
			neighbor = neighbor + current
			if len(map) <= neighbor.x or neighbor.x <= -1 or len(map[0]) <= neighbor.y or neighbor.y <= -1: #neighbor out of bounds
				pass

			elif neighbor in closed_nodes or map[neighbor.x][neighbor.y] in non_navi: #neighbor not navigatable
				pass
			else:
				if neighbor in open_nodes and closed_nodes[current]["g"] + 1 > open_nodes[neighbor]["g"]: #neighbor is slower
					pass
				else:
					open_nodes[neighbor] = {
						"g": closed_nodes[current]["g"] + 1,
						"h": neighbor.get_h(finish),
						"parent": current
					}


def find_tile(map, pos, explorative = False):
	max_dist = 0
	
	non_navi = [0]
	open_nodes = {
		pos: {
			"g": 0,
			"parent": None
		}
	}
	closed_nodes = {}
	while True:
		if len(open_nodes) == 0:
			return max_dist
		
		current = find_lowest_g(open_nodes)
		closed_nodes[current] = open_nodes[current]
		del open_nodes[current]
		
		if map[current.x][current.y] == -1 and not explorative:
			path = []
			while closed_nodes[current]["parent"] is not None:
				path.insert(0, current)
				current = closed_nodes[current]["parent"]
			return path
		
		for neighbor in [Vector(0,1), Vector(1,0), Vector(0,-1), Vector(-1,0)]:
			neighbor = neighbor + current
			if len(map) <= neighbor.x or neighbor.x <= -1 or len(map[0]) <= neighbor.y or neighbor.y <= -1: #neighbor out of bounds
				pass
			elif neighbor in closed_nodes or map[neighbor.x][neighbor.y] in non_navi: #neighbor not navigatable
				pass
			else:
				if neighbor in open_nodes and closed_nodes[current]["g"] + 1 > open_nodes[neighbor]["g"]: #neighbor is slower
					pass
				else:
					max_dist = max(max_dist, closed_nodes[current]["g"] + 1)
					open_nodes[neighbor] = {
						"g": closed_nodes[current]["g"] + 1,
						"parent": current
					}