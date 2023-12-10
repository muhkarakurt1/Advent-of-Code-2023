
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
			current_mapping_dict[(source_range_start, source_range_start + range_length - 1)] = (destination_range_start, destination_range_start + range_length - 1)

		line_number += 1

def find_lowest_location_from_range(initial_seeds, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
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

# print('PART1:',find_lowest_location_from_range(seed_numbers, seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
# 						 light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping))


# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

import numpy as np

# ------------------------------ Sorted mappings ----------------------------- #
seed_to_soil_mapping = dict(sorted(seed_to_soil_mapping.items()))
soil_to_fertilizer_mapping = dict(sorted(soil_to_fertilizer_mapping.items()))
fertilizer_to_water_mapping = dict(sorted(fertilizer_to_water_mapping.items()))
water_to_light_mapping = dict(sorted(water_to_light_mapping.items()))
light_to_temperature_mapping = dict(sorted(light_to_temperature_mapping.items()))
temperature_to_humidity_mapping = dict(sorted(temperature_to_humidity_mapping.items()))
humidity_to_location_mapping = dict(sorted(humidity_to_location_mapping.items()))

all_mappings = [seed_to_soil_mapping, soil_to_fertilizer_mapping, fertilizer_to_water_mapping, water_to_light_mapping,
				light_to_temperature_mapping, temperature_to_humidity_mapping, humidity_to_location_mapping]


# ------------------ Convert interval mapping to 1-1 mapping ----------------- #

test_set = set()

for source, destination in seed_to_soil_mapping.items():
	print('SOURCE:', source)
	test_set.update(list(range(source[0], source[1] + 1)))

print('asdasd')

test_dict = dict.fromkeys(test_set)

print('asdasd')
for source, destination in seed_to_soil_mapping.items():
	print('SOURCE:', source)
	for distance, mapping_value in enumerate(range(source[0], source[1] + 1)):
		test_dict[mapping_value] = destination[0] + distance

print('asdasd')

# ----------------------------- Boundaries ----------------------------- #

def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list

seed_to_soil_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(seed_to_soil_mapping.keys())])
soil_to_fertilizer_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(soil_to_fertilizer_mapping.keys())])
fertilizer_to_water_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(fertilizer_to_water_mapping.keys())])
water_to_light_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(water_to_light_mapping.keys())])
light_to_temperature_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(light_to_temperature_mapping.keys())])
temperature_to_humidity_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(temperature_to_humidity_mapping.keys())])
humidity_to_location_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(humidity_to_location_mapping.keys())])

# ----------------------------- Lower Boundaries ----------------------------- #
seed_to_soil_lower_boundaries = [k[0] for k in seed_to_soil_mapping.keys()]
soil_to_fertilizer_lower_boundaries = [k[0] for k in soil_to_fertilizer_mapping.keys()]
fertilizer_to_water_lower_boundaries = [k[0] for k in fertilizer_to_water_mapping.keys()]
water_to_light_lower_boundaries = [k[0] for k in water_to_light_mapping.keys()]
light_to_temperature_lower_boundaries = [k[0] for k in light_to_temperature_mapping.keys()]
temperature_to_humidity_lower_boundaries = [k[0] for k in temperature_to_humidity_mapping.keys()]
humidity_to_location_lower_boundaries = [k[0] for k in humidity_to_location_mapping.keys()]

# ------------------------------ Value mappings ------------------------------ #
seed_to_soil_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(seed_to_soil_mapping.items())})
soil_to_fertilizer_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(soil_to_fertilizer_mapping.items())})
fertilizer_to_water_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(fertilizer_to_water_mapping.items())})
water_to_light_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(water_to_light_mapping.items())})
light_to_temperature_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(light_to_temperature_mapping.items())})
temperature_to_humidity_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(temperature_to_humidity_mapping.items())})
humidity_to_location_value_mapping = dict({i + 1: v for i, (k,v) in enumerate(humidity_to_location_mapping.items())})

def find_actual_mapping_from_boundaries(mapping_value, upper_boundaries, lower_boundaries, mapping):

	index = np.searchsorted(upper_boundaries, mapping_value, side='left')
	if index not in mapping.keys():
		return mapping_value
	else:
		distance_to_lower_threshold = mapping_value - lower_boundaries[index-1]
		return mapping[index][0] + distance_to_lower_threshold

def combine_mappings(all_mappings):

	final_mapping = all_mappings[0].copy()

	for mapping_number, mapping in enumerate(all_mappings[1:]):

		lower_boundaries = [k[0] for k in mapping.keys()]
		upper_boundaries = flatten_concatenation([[k[0] - 1, k[1]] if i == 0 else [k[1]] for i, k in enumerate(mapping.keys())])

		for source_range, destination_range in final_mapping.items():

			destination_range_start = destination_range[0]
			destination_range_end = destination_range[1]

			start_index = np.searchsorted(upper_boundaries, destination_range_start, side='left')


	return 1

def find_lowest_location_from_boundaries(final_seed_numbers,
										seed_to_soil_upper_boundaries, seed_to_soil_lower_boundaries, seed_to_soil_value_mapping,
										soil_to_fertilizer_upper_boundaries, soil_to_fertilizer_lower_boundaries, soil_to_fertilizer_value_mapping,
										fertilizer_to_water_upper_boundaries, fertilizer_to_water_lower_boundaries, fertilizer_to_water_value_mapping,
										water_to_light_upper_boundaries, water_to_light_lower_boundaries, water_to_light_value_mapping,
										light_to_temperature_upper_boundaries, light_to_temperature_lower_boundaries, light_to_temperature_value_mapping,
										temperature_to_humidity_upper_boundaries, temperature_to_humidity_lower_boundaries, temperature_to_humidity_value_mapping,
										humidity_to_location_upper_boundaries, humidity_to_location_lower_boundaries, humidity_to_location_value_mapping):
	
	lowest_location = 1e13
	for pair_number, seed_info in enumerate(final_seed_numbers):
			range_start = seed_info[0]
			range_length = seed_info[1]
			print('PAIR NUMBER:', pair_number)
			for seed in range(range_start, range_start + range_length):

				soil = find_actual_mapping_from_boundaries(seed, seed_to_soil_upper_boundaries, seed_to_soil_lower_boundaries, seed_to_soil_value_mapping)
				fertilizer = find_actual_mapping_from_boundaries(soil, soil_to_fertilizer_upper_boundaries, soil_to_fertilizer_lower_boundaries, soil_to_fertilizer_value_mapping)
				water = find_actual_mapping_from_boundaries(fertilizer, fertilizer_to_water_upper_boundaries, fertilizer_to_water_lower_boundaries, fertilizer_to_water_value_mapping)
				light = find_actual_mapping_from_boundaries(water, water_to_light_upper_boundaries, water_to_light_lower_boundaries, water_to_light_value_mapping)
				temperature = find_actual_mapping_from_boundaries(light, light_to_temperature_upper_boundaries, light_to_temperature_lower_boundaries, light_to_temperature_value_mapping)
				humidity = find_actual_mapping_from_boundaries(temperature, temperature_to_humidity_upper_boundaries, temperature_to_humidity_lower_boundaries, temperature_to_humidity_value_mapping)
				location = find_actual_mapping_from_boundaries(humidity, humidity_to_location_upper_boundaries, humidity_to_location_lower_boundaries, humidity_to_location_value_mapping)
				# print('SEED:', seed, 'LOCATION:', location)
				if location < lowest_location:
					lowest_location = location

	return lowest_location

print('PART2:',find_lowest_location_from_boundaries(final_seed_numbers,
										seed_to_soil_boundaries, seed_to_soil_lower_boundaries, seed_to_soil_value_mapping,
										soil_to_fertilizer_boundaries, soil_to_fertilizer_lower_boundaries, soil_to_fertilizer_value_mapping,
										fertilizer_to_water_boundaries, fertilizer_to_water_lower_boundaries, fertilizer_to_water_value_mapping,
										water_to_light_boundaries, water_to_light_lower_boundaries, water_to_light_value_mapping,
										light_to_temperature_boundaries, light_to_temperature_lower_boundaries, light_to_temperature_value_mapping,
										temperature_to_humidity_boundaries, temperature_to_humidity_lower_boundaries, temperature_to_humidity_value_mapping,
										humidity_to_location_boundaries, humidity_to_location_lower_boundaries, humidity_to_location_value_mapping))

