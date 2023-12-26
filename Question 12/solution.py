input_file = "input2.txt"

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
with open(input_file) as f:
    damaged_record_springs = []
    group_numbers = []
    for line in f:
        stripped_line = line.strip()
        springs_string, group_numbers_string = stripped_line.split(" ")
        damaged_record_springs.append(springs_string)
        group_numbers_row = group_numbers_string.split(",")
        group_numbers_row = [int(line) for line in group_numbers_row]
        group_numbers.append(group_numbers_row)

from itertools import groupby, product, permutations


def find_contiguous_groups(damaged_record_spring):
    return [len(list(j)) for char, j in groupby(damaged_record_spring) if char == "#"]


def find_number_of_arrangement(damaged_record_spring, group_number):
    count = 0
    all_permutations = find_all_permutations(damaged_record_spring, "#.")

    for permutation in all_permutations:
        if find_contiguous_groups(permutation) == group_number:
            count += 1
    return count


def find_all_permutations(damaged_record_spring, chars):
    all_permutations = []

    for p in map(iter, product(chars, repeat=damaged_record_spring.count("?"))):
        all_permutations.append("".join(c if c != "?" else next(p) for c in damaged_record_spring))

    return all_permutations


def find_number_of_arrangement_sum(damaged_record_springs, group_numbers):
    number_of_arrangement_sum = 0

    for damaged_record_spring, group_number in zip(damaged_record_springs, group_numbers):
        number_of_arrangement_sum += find_number_of_arrangement(damaged_record_spring, group_number)

    return number_of_arrangement_sum


# print('PART 1:', find_number_of_arrangement_sum(damaged_record_springs, group_numbers))

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #
with open(input_file) as f:
    damaged_record_springs = []
    group_numbers = []
    for line in f:
        stripped_line = line.strip()
        springs_string, group_numbers_string = stripped_line.split(" ")
        springs_string = (springs_string + "?") * 4 + springs_string
        group_numbers_string = (group_numbers_string + ",") * 4 + group_numbers_string
        damaged_record_springs.append(springs_string)
        group_numbers_row = group_numbers_string.split(",")
        group_numbers_row = [int(line) for line in group_numbers_row]
        group_numbers.append(group_numbers_row)

from more_itertools import distinct_permutations as idp


def find_count_of_eligible_permutations(damaged_record_spring, group_number):
    starting_characters = "#" * (sum(group_number) - damaged_record_spring.count("#")) + "." * (damaged_record_spring.count("?") - (sum(group_number) - damaged_record_spring.count("#")))
    eligible_character_permutations = ["".join(p) for p in idp(starting_characters)]
    count = 0

    for p in map(iter, eligible_character_permutations):
        permutation = "".join(c if c != "?" else next(p) for c in damaged_record_spring)
        if find_contiguous_groups(permutation) == group_number:
            count += 1

    return count


def find_number_of_arrangement_sum_quicker(damaged_record_springs, group_numbers):
    number_of_arrangement_sum = 0

    for damaged_record_spring, group_number in zip(damaged_record_springs, group_numbers):
        number_of_arrangement_sum += find_count_of_eligible_permutations(damaged_record_spring, group_number)

    return number_of_arrangement_sum


print(
    "PART 2:",
    find_number_of_arrangement_sum_quicker(damaged_record_springs, group_numbers),
)
