input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

with open(input_file) as f:

	race_times = []
	record_distances = []

	for line in f:

		stripped_line = line.strip()
		line_type_string, input_numbers_string = stripped_line.split(':')
		input_numbers = input_numbers_string.split()
		input_numbers = [int(i) for i in input_numbers]
		
		if line_type_string == 'Time':
			race_times.extend(input_numbers)
		elif line_type_string == 'Distance':
			record_distances.extend(input_numbers)

def calculate_number_of_ways(race_time, record_distance):

	number_of_ways = 0

	for button_hold_time in range(race_time + 1):

		gained_speed = button_hold_time
		traveled_distance = gained_speed * (race_time - button_hold_time)
		
		if traveled_distance > record_distance:
			number_of_ways += 1

	return number_of_ways


number_of_ways_multiplication = 1

for race_time, record_distance in zip(race_times, record_distances):
	number_of_ways = calculate_number_of_ways(race_time, record_distance)
	number_of_ways_multiplication *= number_of_ways

print('Part1:', number_of_ways_multiplication)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

with open(input_file) as f:

	for line in f:

		stripped_line = line.strip()
		line_type_string, input_numbers_string = stripped_line.split(':')
		input_number = int(input_numbers_string.replace(' ',''))

		if line_type_string == 'Time':
			race_time = input_number
		elif line_type_string == 'Distance':
			record_distance = input_number

print('Part2:', calculate_number_of_ways(race_time, record_distance))