import numpy as np
import re

input_file = "input2.txt"

def extract_adjacents(board, line_number, indices, len_of_number, number):

	# First line
	if line_number == 0:

		if indices[0] == 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number + 1][ :indices[1] + 2]
			adjacents.extend(board[line_number][indices[1] + 1])
			correct_length = len_of_number + 2

		elif indices[0] == 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number + 1]
			correct_length = len(board)

		elif indices[0] != 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number + 1][(indices[0] - 1) : (indices[1] + 2)]
			adjacents.extend(board[line_number][indices[1] + 1])
			adjacents.extend(board[line_number][indices[0] - 1])
			correct_length = len_of_number + 4

		elif indices[0] != 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number + 1][indices[0] - 1 :]
			adjacents.extend(board[line_number][indices[0] - 1])
			correct_length = len_of_number + 2

	# Middle lines
	elif  0 < line_number < len(board) - 1:
		if indices[0] == 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number - 1][:(indices[1] + 2)]
			adjacents.extend(board[line_number + 1][:(indices[1] + 2)])
			adjacents.extend(board[line_number][indices[1] + 1])
			correct_length = 2 * (len_of_number + 1) + 1

		elif indices[0] == 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number - 1]
			adjacents.extend(board[line_number + 1])
			correct_length = 2 * len(board)

		elif indices[0] != 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number - 1][(indices[0] - 1) : (indices[1] + 2)]
			adjacents.extend(board[line_number + 1][(indices[0] - 1) : (indices[1] + 2)])
			adjacents.extend(board[line_number][indices[1] + 1])
			adjacents.extend(board[line_number][indices[0] - 1])
			correct_length = 2 * (len_of_number + 2) + 2

		elif indices[0] != 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number - 1][(indices[0] - 1) :]
			adjacents.extend(board[line_number + 1][(indices[0] - 1) :])
			adjacents.extend(board[line_number][(indices[0] - 1)])
			correct_length = 2 * (len_of_number + 1) + 1

	# Last line
	else:
		# print('LAST LINE')
		if indices[0] == 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number - 1][ :(indices[1] + 2)]
			adjacents.extend(board[line_number][(indices[1] + 1)])
			correct_length = len_of_number + 2

		elif indices[0] == 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number - 1][ :]
			correct_length = len(board)

		elif indices[0] != 0 and indices[1] != len(board) - 1:
			adjacents = board[line_number - 1][(indices[0] - 1) : (indices[1] + 2)]
			adjacents.extend(board[line_number][indices[1] + 1])
			adjacents.extend(board[line_number][indices[0] - 1])
			correct_length = len_of_number + 4

		elif indices[0] != 0 and indices[1] == len(board) - 1:
			adjacents = board[line_number - 1][indices[0] - 1 : indices[1] + 2]
			adjacents.extend(board[line_number][indices[0] - 1])
			correct_length = len_of_number + 2

	if len(adjacents) != correct_length:
		print('WRONG LINE')

	if '/n' in adjacents:
		print('WTF')

	# if number == 683:
	# 	print('asdasd')
	return adjacents


# Creating a numpy array from the input txt
# with open(input_file, "r") as f:
#     input_array = np.stack([np.fromiter(list(line.strip()), dtype=object) for line in f])
from string import punctuation

board = list(open(input_file))
board = [list(line.strip()) for line in board]
unique_characters = {x for l in board for x in l if not x.isdigit() and x != '.'}

with open(input_file) as f:
	sum_of_part_numbers = 0
	line_number = 0
	for line in f:
		stripped_line = line.strip()
		
		print('Line:', line_number + 1)

		# Find numbers and start-end indices in the line
		idxs_numbers_dict = {int(m.group(0)):[m.start(0), m.end(0) - 1] for m in re.finditer(r'\d+', stripped_line)}

		# Search for adjacents
		for number, indices in idxs_numbers_dict.items():
			# print(number)
			adjacents = extract_adjacents(board, line_number, indices, len(str(number)), number)
			# print(adjacents)
			if not all(ele == '.' for ele in adjacents):
				print(number)
				print('True')
				# print('True')
				# print(number)
				# print(adjacents)
				sum_of_part_numbers += number
			else:
				print(number)
				print('False')

		line_number += 1

print('SUM:',sum_of_part_numbers)

# import math as m, re

# board2 = list(open(input_file))
# chars = {(r, c): [] for r in range(140) for c in range(140)
#                     if board2[r][c] not in '01234566789.'}

# for r, row in enumerate(board2):
#     for n in re.finditer(r'\d+', row):
#         edge = {(r, c) for r in (r-1, r, r+1)
#                        for c in range(n.start()-1, n.end()+1)}

#         for o in edge & chars.keys():
#             chars[o].append(int(n.group()))

# print(sum(sum(p)    for p in chars.values()),
#       sum(m.prod(p) for p in chars.values() if len(p)==2))