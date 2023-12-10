input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

history_numbers_list = []

with open(input_file) as f:

	line_number = 0
	
	for line in f:
		
		stripped_line = line.strip()
		
		history_numbers_string = stripped_line.split()
		history_numbers = [int(history_number_string) for history_number_string in history_numbers_string]
		history_numbers_list.append(history_numbers)

from itertools import pairwise

def extrapolate_future_history(history_numbers):

	history_numbers_copy = history_numbers.copy()
	differences_list = [history_numbers_copy]
	current_differences = history_numbers_copy

	while not all(ele == 0 for ele in current_differences):
		current_differences = [y - x for x, y in pairwise(current_differences)]
		differences_list.append(current_differences)

	reversed_differences = list(reversed(differences_list))
	for i in range(len(reversed_differences)):
		if i == 0:
			reversed_differences[i].append(0)
		else:
			reversed_differences[i].append(reversed_differences[i-1][-1] + reversed_differences[i][-1])

	return reversed_differences[-1][-1]

sum_of_extrapolated_values= 0
for history_numbers in history_numbers_list:
	
	next_value = extrapolate_future_history(history_numbers)
	sum_of_extrapolated_values += next_value

print('PART1:', sum_of_extrapolated_values)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

def extrapolate_past_history(history_numbers):

	history_numbers_copy = history_numbers.copy()
	differences_list = [history_numbers_copy]
	current_differences = history_numbers_copy

	while not all(ele == 0 for ele in current_differences):
		current_differences = [y - x for x, y in pairwise(current_differences)]
		differences_list.append(current_differences)

	differences_list_copy = differences_list.copy()
	reversed_differences = list(reversed(differences_list_copy))
	for i in range(len(reversed_differences)):
		if i == 0:
			reversed_differences[i].insert(0, 0)
		else:
			reversed_differences[i].insert(0, reversed_differences[i][0] - reversed_differences[i-1][0])

	return reversed_differences[-1][0]

sum_of_extrapolated_values= 0
for history_numbers in history_numbers_list:
	
	previous_value = extrapolate_past_history(history_numbers)
	sum_of_extrapolated_values += previous_value

print('PART2:', sum_of_extrapolated_values)
