# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

import re

with open('input.txt') as f:

	possible_game_id_sum = 0

	for line in f:

		game_is_possible = True
		stripped_line = line.strip()

		# Splitting the game number and the actual game
		game_number_string, game_string = stripped_line.split(':')
		_, game_number = game_number_string.split()
		game_number = int(game_number)

		# Analyzing the game
		cube_sets = game_string.replace(" ", "").split(';')
		buckets = {'blue':0, 'green':0, 'red':0}
		for cube_set in cube_sets:
			cube_infos = cube_set.split(',')
			for cube_info in cube_infos:
				_, number, color = re.split('(\d+)', cube_info)
				if int(number) > buckets[color]:
					buckets[color] = int(number)
		
		# Check if the game is possible
		for color, max_number in buckets.items():
			if color == 'red' and max_number > 12:
				game_is_possible = False
			if color == 'green' and max_number > 13:
				game_is_possible = False
			if color == 'blue' and max_number > 14:
				game_is_possible = False
		
		if game_is_possible:
			possible_game_id_sum += game_number
			# print(game_number)

print(possible_game_id_sum)
# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

with open('input.txt') as f:

	sum_of_powers = 0

	for line in f:

		game_power = 1
		stripped_line = line.strip()

		# Splitting the game number and the actual game
		game_number_string, game_string = stripped_line.split(':')
		_, game_number = game_number_string.split()
		game_number = int(game_number)

		# Analyzing the game
		cube_sets = game_string.replace(" ", "").split(';')
		buckets = {'blue':0, 'green':0, 'red':0}
		for cube_set in cube_sets:
			cube_infos = cube_set.split(',')
			for cube_info in cube_infos:
				_, number, color = re.split('(\d+)', cube_info)
				if int(number) > buckets[color]:
					buckets[color] = int(number)
		
		# Calculate the power of the game
		for color, max_number in buckets.items():
			game_power = game_power * max_number
		
		sum_of_powers += game_power

print(sum_of_powers)