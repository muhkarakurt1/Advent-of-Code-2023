input_file = 'input2.txt'
import random
# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
class Pipe:

	def __init__(self, coordinates, pipe_symbol, connection_mapping) -> None:
		self.coordinates = coordinates
		self.pipe_symbol = pipe_symbol
		self.connection_mapping = connection_mapping
 
class Board:

	def __init__(self, board_input, num_of_rows, num_of_cols) -> None:
		self.num_of_rows = num_of_rows
		self.num_of_cols = num_of_cols
		self.pipes = [[Pipe((row_number, col_number), pipe_symbol,self.get_pipe_connection_mapping(pipe_symbol)) for col_number, pipe_symbol in enumerate(row)] for row_number, row in enumerate(board_input)]
		self.pipes_in_loop = None
		self.coordinates_in_loop = None
		self.distance_to_loop_start = None

	def get_pipe_connection_mapping(self, pipe_symbol):

		if pipe_symbol == '|':
			return ('N','S')
		elif pipe_symbol == '-':
			return ('E','W')
		elif pipe_symbol == 'L':
			return ('N','E')
		elif pipe_symbol == 'J':
			return ('N','W')
		elif pipe_symbol == '7':
			return ('S','W')
		elif pipe_symbol == 'F':
			return ('S','E')
		if pipe_symbol == '.':
			return ('','')
		else:
			return None
	
	def fill_start_location_connection_mapping(self, row_number, column_number):
		self.pipes[row_number][column_number].connection_mapping = tuple(self.find_possible_movements(row_number, column_number))
	
	def find_possible_movements(self, row_number, column_number):

		x = column_number
		y = row_number

		possible_movements = []
		for dx, dy, movement_direction, opposite_direction in ((1,0,'E','W'), (-1,0,'W','E'), (0,1,'S','N'), (0,-1,'N','S')):

			if (x + dx > len(self.pipes) - 1) or (x + dx < 0) or (y+ dy > len(self.pipes) - 1) or (y+ dy < 0):
				continue
			else:
				if opposite_direction in self.pipes[y+ dy][x + dx].connection_mapping:
					possible_movements.append(movement_direction)
		
		return possible_movements
	
	def fill_loop_objects(self, starting_pipe):

		opposite_directions = {'W':'E','E':'W','N':'S','S':'N'}
		if self.pipes_in_loop is None:
			self.pipes_in_loop = [starting_pipe]

		current_pipe = self.pipes_in_loop[-1]

		while current_pipe != starting_pipe or len(self.pipes_in_loop) == 1:
			# print(current_pipe.coordinates)
			current_pipe_coordinates = current_pipe.coordinates

			# Find next direction and its opposite
			if len(self.pipes_in_loop) == 1:
				next_direction = random.choice(starting_pipe.connection_mapping)
				opposite_direction = opposite_directions[next_direction]
			else:
				next_direction = [direction for direction in current_pipe.connection_mapping if direction!=opposite_direction][0]
				opposite_direction = opposite_directions[next_direction]

			# Move towards the next direction
			if next_direction == 'E':
				next_pipe = self.pipes[current_pipe_coordinates[0]][current_pipe_coordinates[1] + 1]
				self.pipes_in_loop.append(next_pipe)
				current_pipe = next_pipe
			elif next_direction == 'W':
				next_pipe = self.pipes[current_pipe_coordinates[0]][current_pipe_coordinates[1] - 1]
				self.pipes_in_loop.append(next_pipe)
				current_pipe = next_pipe
			elif next_direction == 'N':
				next_pipe = self.pipes[current_pipe_coordinates[0] - 1][current_pipe_coordinates[1]]
				self.pipes_in_loop.append(next_pipe)
				current_pipe = next_pipe
			elif next_direction == 'S':
				next_pipe = self.pipes[current_pipe_coordinates[0] + 1][current_pipe_coordinates[1]]
				self.pipes_in_loop.append(next_pipe)
				current_pipe = next_pipe

	def fill_loop_coordinates(self):
		self.coordinates_in_loop = [pipe.coordinates for pipe in self.pipes_in_loop]

	def fill_step_size(self):

		reversed_loop = self.pipes_in_loop[::-1]
		
		distances_from_left = {pipe.coordinates: left_distance for left_distance, pipe in enumerate(self.pipes_in_loop) if pipe.pipe_symbol != 'S'}
		distances_from_right = {pipe.coordinates: right_distance for right_distance, pipe in enumerate(reversed_loop) if pipe.pipe_symbol != 'S'}

		self.distance_to_loop_start = {pipe.coordinates: min(distances_from_left[pipe.coordinates], distances_from_right[pipe.coordinates]) for _,pipe in enumerate(self.pipes_in_loop) if pipe.pipe_symbol != 'S'}


board_input = list(open(input_file))
board_input = [list(line.strip()) for line in board_input]
num_of_rows, num_of_cols = len(board_input), len(board_input[0])
start_location = [(row_number, column_number) for row_number, row in enumerate(board_input) for column_number, pipe in enumerate(row) if pipe =='S'][0]

board = Board(board_input, num_of_rows, num_of_cols)
start_location_row_number, start_location_column_number = start_location[0], start_location[1]
board.fill_start_location_connection_mapping(start_location_row_number, start_location_column_number)
starting_pipe_obj = [pipe_obj for row in board.pipes for pipe_obj in row if pipe_obj.pipe_symbol == 'S'][0]

board.fill_loop_objects(starting_pipe_obj)
board.fill_loop_coordinates()
board.fill_step_size()
print('PART1:', max(board.distance_to_loop_start.values()))
# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

