input_file = 'input2.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
class Pipe:

	def __init__(self, coordinates, pipe_symbol, connection_mapping) -> None:
		self.coordinates = coordinates
		self.pipe_symbol = pipe_symbol
		self.connection_mapping = connection_mapping
		self.possible_movements = None

class Board:

	def __init__(self, board_input) -> None:
		self.pipes = [[Pipe((row_number, col_number), pipe_symbol,self.get_pipe_connection_mapping(pipe_symbol)) for col_number, pipe_symbol in enumerate(row)] for row_number, row in enumerate(board_input)]
		self.pipes_in_loop = []

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
					possible_movements.append(self.pipes[y+ dy][x + dx])
		
		return possible_movements
	
	def fill_possible_movements(self):
		num_of_rows = len(self.pipes)
		num_of_cols = len(self.pipes[0])
		for row_number in range(num_of_rows):
			for col_number in range(num_of_cols):
				self.pipes[row_number][col_number].possible_movements = self.find_possible_movements(row_number, col_number)

	def find_loop(self, starting_pipe):

		current_pipe = starting_pipe
		next_pipe = None
		
		self.pipes_in_loop = [starting_pipe]

		while next_pipe != starting_pipe.id:

			next_pipe = 1

		pass
board_input = list(open(input_file))
board_input = [list(line.strip()) for line in board_input]
start_location = [(row_number, column_number) for row_number, row in enumerate(board_input) for column_number, pipe in enumerate(row) if pipe =='S'][0]

board = Board(board_input)
start_location_row_number, start_location_column_number = start_location[0], start_location[1]
board.fill_start_location_connection_mapping(start_location_row_number, start_location_column_number)
board.fill_possible_movements()

starting_pipe_obj = [pipe_obj for row in board.pipes for pipe_obj in row if pipe_obj.pipe_symbol == 'S'][0]
board.find_loop(starting_pipe_obj)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #
