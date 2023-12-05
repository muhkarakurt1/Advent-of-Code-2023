import numpy as np
import re

input_file = "input.txt"

def extract_adjacents(input_array, line_number, indices):

	# First line
	if line_number == 0:

		if indices[0] == 0 and indices[1] != input_array.shape[1] - 1:
			adjacents = input_array[line_number + 1, :indices[1] + 2]
			adjacents = np.append(adjacents, input_array[line_number, indices[1] + 1])
		
		elif indices[0] == 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number + 1, :]

		elif indices[0] != 0 and indices[1] != input_array.shape[1] - 1:
			adjacents = input_array[line_number + 1, indices[0] - 1 : indices[1] + 2]
			adjacents = np.append(adjacents,input_array[line_number, indices[1] + 1])
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])

		elif indices[0] != 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number + 1, indices[0] - 1 :]
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])

	# Middle lines
	elif line_number < input_array.shape[0] - 1:
		if indices[0] == 0 and indices[1] != input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1,  :(indices[1] + 2)]
			adjacents = np.append(adjacents,input_array[line_number + 1,  :(indices[1] + 2)])
			adjacents = np.append(adjacents,input_array[line_number, indices[1] + 1])
		
		elif indices[0] == 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, :]
			adjacents = np.append(adjacents,input_array[line_number + 1, :])

		elif indices[0] != 0 and indices[1] != input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, (indices[0] - 1) : (indices[1] + 2)]
			adjacents = np.append(adjacents,input_array[line_number + 1, (indices[0] - 1) : (indices[1] + 2)])
			adjacents = np.append(adjacents,input_array[line_number, indices[1] + 1])
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])

		elif indices[0] != 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, indices[0] - 1 :]
			adjacents = np.append(adjacents,input_array[line_number + 1, indices[0] - 1 :])
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])
	
	# Last line
	else:
		if indices[0] == 0 and indices[1] != input_array.shape[1] - 1:

			adjacents = input_array[line_number - 1, indices[0] : indices[1] + 2]
			adjacents = np.append(adjacents,input_array[line_number, indices[1] + 1])
		
		elif indices[0] == 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, :]

		elif indices[0] != 0 and indices[1] != input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, indices[0] - 1 : indices[1] + 2]
			adjacents = np.append(adjacents,input_array[line_number, indices[1] + 1])
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])

		elif indices[0] != 0 and indices[1] == input_array.shape[1] - 1:
			adjacents = input_array[line_number - 1, indices[0] - 1 : indices[1] + 2]
			adjacents = np.append(adjacents,input_array[line_number, indices[0] - 1])
	return adjacents


# Creating a numpy array from the input txt
with open(input_file, "r") as f:
    input_array = np.stack([np.fromiter(list(line.strip()), dtype=object) for line in f])

with open(input_file) as f:
	sum_of_part_numbers = 0
	line_number = 0
	for line in f:
		stripped_line = line.strip()
		
		print('Line:', line_number + 1)
		# Find numbers and start-end indices in the line
		idxs_numbers_dict = {int(m.group(0)):[m.start(0), m.end(0) - 1] for m in re.finditer("\d+", stripped_line)}
		
		
		# Search for adjacents
		for number, indices in idxs_numbers_dict.items():
			print(number)
			adjacents = extract_adjacents(input_array, line_number, indices)
			print(adjacents)
			if not np.all(adjacents == '.'):
				# print(number)
				# print(adjacents)
				sum_of_part_numbers += number

		line_number += 1

print('SUM:',sum_of_part_numbers)

import math as m, re

board = list(open(input_file))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))