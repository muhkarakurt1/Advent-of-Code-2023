
# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
calibration_sum = 0
with open('input.txt') as f:
	for line in f:
		digits = ''
		stripped_line = line.strip()
		for char in stripped_line:
			if char.isdigit():
				digits += char
		calibration = int(digits[0] + digits[-1])
		# print(calibration)
		calibration_sum += calibration

print(calibration_sum)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

from word2number import w2n
valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# for valid_digit in valid_digits:
# 	print(w2n.word_to_num(valid_digit))

calibration_sum = 0
with open('input.txt') as f:
	for line in f:
		digits = {}
		stripped_line = line.strip()
		for idx, char in enumerate(stripped_line):
			if char.isdigit():
				digits[idx] = int(char)
		for valid_digit in valid_digits:
			res = [(i,w2n.word_to_num(valid_digit)) for i in range(len(stripped_line)) if stripped_line.startswith(valid_digit, i)]
			digits.update(res)
		print('Digits:',digits)
		calibration = int(str(digits[min(digits)]) + str(digits[max(digits)]))
		print('Calibration:',calibration)
		calibration_sum += calibration

print(calibration_sum)