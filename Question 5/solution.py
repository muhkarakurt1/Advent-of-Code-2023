
input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #

with open(input_file) as f:

	line_number = 1

	seed_to_soil_mapping = {}
	soil_to_fertilizer_mapping = {}
	fertilizer_to_water_mapping = {}
	water_to_light_mapping = {}
	light_to_temperature_mapping = {}
	temperature_to_humidity_mapping = {}
	humidity_to_location_mapping = {}

	current_mapping_dict = seed_to_soil_mapping
	
	for line in f:
		print('Line:', line_number)
		stripped_line = line.strip()

		# First line
		if line_number == 1:
			
			_, seed_numbers_string = stripped_line.split(':')
			seed_numbers = seed_numbers_string.split()
			seed_numbers = [int(i) for i in seed_numbers]
			seed_number_range_start = seed_numbers[0::2]
			seed_number_range_length = seed_numbers[1::2]
			
			# PART 2
			final_seed_numbers = [(range_start, range_length) for range_start, range_length in zip(seed_number_range_start, seed_number_range_length)]

		# Empty line
		elif not stripped_line:
			print('EMPTY LINE')
		
		# Mapping text
		elif not stripped_line[0].isdigit():
			mapping_string, _ = stripped_line.split()
			map_from, _, map_to = mapping_string.split('-')

			# Conditions
			if map_from == 'seed' and map_to == 'soil':
				current_mapping_dict = seed_to_soil_mapping
			elif map_from == 'soil' and map_to == 'fertilizer':
				current_mapping_dict = soil_to_fertilizer_mapping
			elif map_from == 'fertilizer' and map_to == 'water':
				current_mapping_dict = fertilizer_to_water_mapping
			elif map_from == 'water' and map_to == 'light':
				current_mapping_dict = water_to_light_mapping
			elif map_from == 'light' and map_to == 'temperature':
				current_mapping_dict = light_to_temperature_mapping
			elif map_from == 'temperature' and map_to == 'humidity':
				current_mapping_dict = temperature_to_humidity_mapping
			elif map_from == 'humidity' and map_to == 'location':
				current_mapping_dict = humidity_to_location_mapping

		# Line with numbers
		else:
			split_line = stripped_line.split()
			destination_range_start, source_range_start, range_length = [int(i) for i in split_line]
			
			# for i in range(range_length):
			# 	current_mapping_dict[source_range_start + i] = destination_range_start + i

			current_mapping_dict[(source_range_start, source_range_start + range_length - 1)] = (destination_range_start, destination_range_start + range_length - 1)

		line_number += 1

def find_lowest_location(initial_seeds, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
						 light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping):
	
	lowest_location = 1e13
	for seed in initial_seeds:
		
		soil = find_actual_mapping_from_range(seed, seed_to_soil_mapping)
		fertilizer = find_actual_mapping_from_range(soil, soil_to_fertilizer_mapping)
		water = find_actual_mapping_from_range(fertilizer, fertilizer_to_water_mapping)
		light = find_actual_mapping_from_range(water, water_to_light_mapping)
		temperature = find_actual_mapping_from_range(light, light_to_temperature_mapping)
		humidity = find_actual_mapping_from_range(temperature, temperature_to_humidity_mapping)
		location = find_actual_mapping_from_range(humidity, humidity_to_location_mapping)

		print('SEED:', seed, 'LOCATION:', location)
		if location < lowest_location:
			lowest_location = location

	return lowest_location

def find_actual_mapping_from_range(mapping_value, mapping):

	mapping_found = False
	for source_range, destination_range in mapping.items():
		if source_range[0] <= mapping_value and mapping_value <= source_range[1]:
			length_to_source_start = mapping_value - source_range[0]
			mapped_value = destination_range[0] + length_to_source_start
			mapping_found = True
			break
	return mapped_value if mapping_found else mapping_value

# print('PART1:',find_lowest_location(seed_numbers, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
# 						 light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping))


# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

def find_lowest_location2(final_seed_numbers, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
						 light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping):
	
	lowest_location = 1e13
	for pair_number, seed_info in enumerate(final_seed_numbers):
			range_start = seed_info[0]
			range_length = seed_info[1]
			print('PAIR NUMBER:', pair_number)
			for seed in range(range_start, range_start + range_length):

				soil = find_actual_mapping_from_range(seed, seed_to_soil_mapping)
				fertilizer = find_actual_mapping_from_range(soil, soil_to_fertilizer_mapping)
				water = find_actual_mapping_from_range(fertilizer, fertilizer_to_water_mapping)
				light = find_actual_mapping_from_range(water, water_to_light_mapping)
				temperature = find_actual_mapping_from_range(light, light_to_temperature_mapping)
				humidity = find_actual_mapping_from_range(temperature, temperature_to_humidity_mapping)
				location = find_actual_mapping_from_range(humidity, humidity_to_location_mapping)
				# print('SEED:', seed, 'LOCATION:', location)
				if location < lowest_location:
					lowest_location = location

	return lowest_location

print('PART2:',find_lowest_location2(final_seed_numbers, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
						 light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping))

