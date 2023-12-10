input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
with open(input_file) as f:

	node_connections = {}
	line_number = 0
	directions = ''
	for line in f:
		
		stripped_line = line.strip()
		
		# First line
		if line_number == 0:
			directions = stripped_line

		# Empty line
		elif not stripped_line:
			pass
		
		else:
			starting_node, left_right_connections = stripped_line.split('=')
			starting_node = starting_node.strip()
			left_connection, right_connection = left_right_connections.split(',')
			left_connection = left_connection.translate({ord(x): '' for x in list('() ')})
			right_connection = right_connection.translate({ord(x): '' for x in list('() ')})
			node_connections[starting_node] = (left_connection, right_connection)
		line_number += 1


def follow_directions(node_connections, directions):

	current_location = 'AAA'
	step_number = 0

	while current_location != 'ZZZ':
		idx = step_number % len(directions)
		current_location = node_connections[current_location][1] if directions[idx] == 'R' else node_connections[current_location][0]
		step_number += 1
		if current_location == 'ZZZ':
			return step_number
		
# print('PART 1:', follow_directions(node_connections, directions))

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

from datetime import datetime
import math
def follow_ghost_directions(node_connections, directions):

	starting_nodes = [node for node in node_connections if node[-1] == 'A']
	minimum_step_numbers = {}

	for location in starting_nodes:

		step_number = 0
		current_location = location

		while current_location[-1] != 'Z':
			idx = step_number % len(directions)
			if directions[idx] == 'R':
				current_location = node_connections[current_location][1]
			else:
				current_location = node_connections[current_location][0]
			step_number += 1
		
		minimum_step_numbers[location] = step_number
		print('Starting Node:', location, 'Step Number:', step_number)
	integer_step_numbers = [int(value) for value in minimum_step_numbers.values()]
	
	return math.lcm(*map(int, integer_step_numbers))
		

	# while not all([location[-1] == 'Z' for location in current_locations]):
	# 	idx = step_number % len(directions)
	# 	if directions[idx] == 'R':
	# 		current_locations = [node_connections[location][1] for location in current_locations]
	# 	else:
	# 		current_locations = [node_connections[location][0] for location in current_locations]
	# 	step_number += 1
	# return step_number

print('Starting Time:', datetime.now())
print('PART 2 Answer:', follow_ghost_directions(node_connections, directions))
print('Ending Time:', datetime.now())
