
def get_index(layer, rows, columns):
	return layer * rows * columns + row * columns + rows


def file_to_layers(file_name, size):
	with open(file_name, "r") as input_file:
		input_string = input_file.read()
		layers = []
		for i in range(len(input_string) // size):
			layers.append([int(x) for x in input_string[i * size:(i + 1) * size]])
		return layers


def combine_layers(layers):
	final_image = []
	for pixel in range(len(layers[0])):
		for layer in layers:
			if layer[pixel] != 2:
				final_image.append(layer[pixel])
				break
	
	return final_image


def layer_to_image(layer, columns):
	i = 0
	image = ""
	for pixel in layer:
		if pixel == 1:
			image += '#'
		else:
			image += ' '
		
		i += 1
		
		if i == columns:
			image += "\n"
			i = 0
	
	return image


intlists = file_to_layers("day8_input.txt", 6 * 25)
print(layer_to_image(combine_layers(intlists), 25))