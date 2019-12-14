from functools import reduce
# layer = i // (rows * columns)
# column = i % columns
# row = i // columns
def get_index(layer, rows, columns):
	return layer * rows * columns + row * columns + rows

def file_to_intlists(file_name, rows, columns):
	with open(file_name, "r") as input_file:
		input_string = input_file.read()
		lists = []
		for i in range(len(input_string) // (rows * columns)):
			lists.append([int(x) for x in input_string[i * (rows * columns):(i + 1) * (rows * columns)]])
		return lists

def increment_element(list, position):
	while(len(list) < position + 1):
		list.append(0)
	list[position] += 1

def count_intlist(intlists):
	summaries = []
	for ints in intlists:
		summary = []
		for int in ints:
			increment_element(summary, int)
		summaries.append(summary)
	return summaries

def min_list_by_first_index(list1, list2):
	if list1[0] < list2[0]:
		return list1
	return list2


intlists = count_intlist(file_to_intlists("day8_input.txt", 6, 25))
min0s = reduce(min_list_by_first_index, intlists)
print(min0s[1] * min0s[2])

	