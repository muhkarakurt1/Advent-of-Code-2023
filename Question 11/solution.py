input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

image_input = list(open(input_file))
image_input = [list(line.strip()) for line in image_input]

def expand_universe(image_input):
	
	expanded_image_input = image_input.copy()

	# Empty rows
	empty_row_idxs = [idx for idx, row in enumerate(image_input) if len(set(row)) == 1]
	
	# Empty columns
	empty_column_idxs = [n for n in range(len(image_input[0])) if len(set([el[n] for el in image_input])) == 1]

	# Insert empty rows
	for row_idx in list(reversed(empty_row_idxs)):
		expanded_image_input.insert(row_idx, ['.' for _ in range(len(image_input[0]))])

	# Insert empty columns
	for col_idx in list(reversed(empty_column_idxs)):
		for row in expanded_image_input:
			row.insert(col_idx, '.')
	
	return expanded_image_input

def find_shortest_path_length(x_coordinates, y_coordinates):
	return abs(x_coordinates[1] - x_coordinates[0]) + abs(y_coordinates[1] - y_coordinates[0])

def find_galaxy_coordinates(image_input):
	return [(col_idx, row_idx) for row_idx, row in enumerate(image_input) for col_idx, character in enumerate(row) if character == '#']

def find_sum_of_shortest_paths(galaxy_coordinates, num_of_points):
	sum_of_shortest_paths = 0

	for i in range(num_of_points):
		for j in range(i+1, num_of_points):
			sum_of_shortest_paths += find_shortest_path_length((galaxy_coordinates[i][0], galaxy_coordinates[j][0]), (galaxy_coordinates[i][1], galaxy_coordinates[j][1]))

	return sum_of_shortest_paths

expanded_image_input = expand_universe(image_input)
galaxy_coordinates = find_galaxy_coordinates(expanded_image_input)
sum_of_shortest_paths = find_sum_of_shortest_paths(galaxy_coordinates, len(galaxy_coordinates))
print('PART1:', sum_of_shortest_paths)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

def expand_universe_n_times(image_input, n): #TOO SLOW
	
	expanded_image_input = image_input.copy()

	# Empty rows
	empty_row_idxs = [idx for idx, row in enumerate(image_input) if len(set(row)) == 1]
	
	# Empty columns
	empty_column_idxs = [n for n in range(len(image_input[0])) if len(set([el[n] for el in image_input])) == 1]

	# Insert empty rows
	for row_idx in list(reversed(empty_row_idxs)):
		for _ in range(n-1):
			expanded_image_input.insert(row_idx, ['.' for _ in range(len(image_input[0]))])

	# Insert empty columns
	for col_idx in list(reversed(empty_column_idxs)):
		for _ in range(n-1):
			for row in expanded_image_input:
				row.insert(col_idx, '.')
		
	return expanded_image_input

def find_empty_indices(image_input):

	# Empty rows
	empty_row_idxs = [idx for idx, row in enumerate(image_input) if len(set(row)) == 1]
	
	# Empty columns
	empty_column_idxs = [n for n in range(len(image_input[0])) if len(set([el[n] for el in image_input])) == 1]

	return empty_row_idxs, empty_column_idxs

def find_sum_of_expanded_shortest_paths(galaxy_coordinates, empty_row_idxs, empty_column_idxs, expansion_rate, num_of_points):
	sum_of_shortest_paths = 0

	for i in range(num_of_points):
		for j in range(i+1, num_of_points):
			sum_of_shortest_paths += find_expanded_shortest_path_length((galaxy_coordinates[i][0], galaxy_coordinates[j][0]), (galaxy_coordinates[i][1], galaxy_coordinates[j][1]),
															   empty_row_idxs, empty_column_idxs, expansion_rate)

	return sum_of_shortest_paths

def find_expanded_shortest_path_length(x_coordinates, y_coordinates, empty_row_idxs, empty_column_idxs, expansion_rate):

	shortest_path = 0
	
	# X distance
	if x_coordinates[1] - x_coordinates[0] >= 0:
		big_x, small_x = x_coordinates[1], x_coordinates[0]
	else:
		big_x, small_x = x_coordinates[0], x_coordinates[1]
	number_of_empty_cols_between = len([empty_col_idx for empty_col_idx in empty_column_idxs if small_x < empty_col_idx < big_x])
	x_distance = abs(x_coordinates[1] - x_coordinates[0]) + number_of_empty_cols_between * (expansion_rate - 1)
	shortest_path += x_distance

	# Y distance
	if y_coordinates[1] - y_coordinates[0] >= 0:
		big_y, small_y = y_coordinates[1], y_coordinates[0]
	else:
		big_y, small_y = y_coordinates[0], y_coordinates[1]
	number_of_empty_rows_between = len([empty_row_idx for empty_row_idx in empty_row_idxs if small_y < empty_row_idx < big_y])
	y_distance = abs(y_coordinates[1] - y_coordinates[0]) + number_of_empty_rows_between * (expansion_rate - 1)
	shortest_path += y_distance

	return shortest_path

image_input = list(open(input_file))
image_input = [list(line.strip()) for line in image_input]

expansion_rate = 1000000
galaxy_coordinates = find_galaxy_coordinates(image_input)
empty_row_idxs, empty_column_idxs = find_empty_indices(image_input)
sum_of_shortest_paths = find_sum_of_expanded_shortest_paths(galaxy_coordinates, empty_row_idxs, empty_column_idxs, expansion_rate, len(galaxy_coordinates))
print('PART2:', sum_of_shortest_paths)