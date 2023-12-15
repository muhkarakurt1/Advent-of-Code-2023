input_file = 'input2.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
with open(input_file) as f:
	damaged_record_springs = []
	group_numbers = []
	for line in f:
		stripped_line = line.strip()
		springs_string, group_numbers_string = stripped_line.split(' ')
		damaged_record_springs.append(springs_string)
		group_numbers_row = group_numbers_string.split(",")
		group_numbers_row = [int(line) for line in group_numbers_row]
		group_numbers.append(group_numbers_row)
		
print('asdasd')

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #
