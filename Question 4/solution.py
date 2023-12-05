
input_file = "input.txt"

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

def calc_matches_and_points(winner_numbers, your_numbers):

	match_count = 0
	for number in your_numbers:
		if number in winner_numbers:
			match_count += 1

	points = (2 ** (match_count - 1)) if match_count != 0 else 0

	return match_count, points

with open(input_file) as f:
	sum_of_points = 0
	for line in f:
		stripped_line = line.strip()

		# Splitting the game number and the actual game
		card_number_string, card_string = stripped_line.split(':')
		_, card_number = card_number_string.split()
		card_number = int(card_number)

		# Analyzing the game
		winner_numbers_string, your_numbers_string  = card_string.split('|')

		winner_numbers = winner_numbers_string.split()
		winner_numbers = [int(i) for i in winner_numbers]
		your_numbers = your_numbers_string.split()
		your_numbers = [int(i) for i in your_numbers]

		_, points = calc_matches_and_points(winner_numbers, your_numbers)
		# print(points)
		sum_of_points += points

print('TOTAL POINTS:', sum_of_points)


# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

num_lines = sum(1 for _ in open(input_file))

with open(input_file) as f:

	total_number_of_scrathcards = 0
	total_cards_won = {i : 1 for i in range(1, num_lines + 1)}

	for line in f:
		stripped_line = line.strip()

		# Splitting the game number and the actual game
		card_number_string, card_string = stripped_line.split(':')
		_, card_number = card_number_string.split()
		card_number = int(card_number)

		# Analyzing the game
		winner_numbers_string, your_numbers_string  = card_string.split('|')

		winner_numbers = winner_numbers_string.split()
		winner_numbers = [int(i) for i in winner_numbers]
		your_numbers = your_numbers_string.split()
		your_numbers = [int(i) for i in your_numbers]

		matches, _ = calc_matches_and_points(winner_numbers, your_numbers)
		if matches > 0:
			for i in range(1, matches + 1):
				if (card_number + i) in total_cards_won:
					total_cards_won[card_number + i] += total_cards_won[card_number] * 1


print(sum(total_cards_won.values()))


