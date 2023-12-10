input_file = 'input.txt'

# ---------------------------------------------------------------------------- #
#                                    Part 1                                    #
# ---------------------------------------------------------------------------- #
from collections import Counter

with open(input_file) as f:

	hands_and_bids = {}

	for line in f:

		stripped_line = line.strip()
		cards, bid = stripped_line.split()
		bid = int(bid)
		hands_and_bids[cards] = bid

def find_hand_type(hand):

	counts_dict = Counter(hand)
	sorted_tuples = sorted(counts_dict.items(), key=lambda x:x[1], reverse=True)
	sorted_values = [x[1] for x in sorted_tuples]

	if sorted_values == [5]:
		return 'quintuple'
	elif sorted_values == [4,1]:
		return 'quads'
	elif sorted_values == [3,2]:
		return 'full_house'
	elif sorted_values == [3,1,1]:
		return 'triple'
	elif sorted_values == [2,2,1]:
		return 'two_pair'
	elif sorted_values == [2,1,1,1]:
		return 'pair'
	elif sorted_values == [1,1,1,1,1]:
		return 'high_card'

hand_and_types = {}
for hand in hands_and_bids.keys():
	hand_type = find_hand_type(hand)
	hand_and_types[hand] = hand_type

winning_order = list(reversed(['quintuple', 'quads', 'full_house', 'triple', 'two_pair', 'pair', 'high_card']))
card_rankings = list('AKQJT98765432')

def calculate_total_winnings(hand_and_types, hands_and_bids, card_rankings):

	hand_ranks = dict.fromkeys(hand_and_types.keys())
	hand_rank = 1
	total_winnings = 0

	for hand_type in winning_order:
		relevant_hands = [k for k, v in hand_and_types.items() if v == hand_type]
		sorted_relevant_hands = sorted(relevant_hands, key=lambda word: [card_rankings.index(c) for c in word], reverse=True)
		for hand in sorted_relevant_hands:
			hand_ranks[hand] = hand_rank
			hand_rank += 1
	
	for hand, rank in hand_ranks.items():
		total_winnings += rank * hands_and_bids[hand]
	
	return hand_ranks, total_winnings

# print(hand_and_types)

hand_rankings, total_winnings = calculate_total_winnings(hand_and_types, hands_and_bids, card_rankings)
# print('Sorted Rankings Part 1:', sorted(hand_rankings.items(), key=lambda x:x[1]))
print('Total Winnings Part 1:', total_winnings)

# ---------------------------------------------------------------------------- #
#                                    Part 2                                    #
# ---------------------------------------------------------------------------- #

card_rankings_with_joker = list('AKQT98765432J')
cards_without_joker = list('AKQT98765432')

def find_hand_type_with_joker(hand):

	counts_dict = Counter(hand)

	if 'J' in counts_dict.keys():
		number_of_jokers = counts_dict['J']
		if number_of_jokers == 5:
			return 'quintuple'
		del counts_dict['J']
		maximum_count_card_without_joker = max(counts_dict.items(), key=lambda x: x[1])
		counts_dict[maximum_count_card_without_joker[0]] += number_of_jokers
		
	sorted_tuples = sorted(counts_dict.items(), key=lambda x:x[1], reverse=True)
	sorted_values = [x[1] for x in sorted_tuples]

	if sorted_values == [5]:
		return 'quintuple'
	elif sorted_values == [4,1]:
		return 'quads'
	elif sorted_values == [3,2]:
		return 'full_house'
	elif sorted_values == [3,1,1]:
		return 'triple'
	elif sorted_values == [2,2,1]:
		return 'two_pair'
	elif sorted_values == [2,1,1,1]:
		return 'pair'
	elif sorted_values == [1,1,1,1,1]:
		return 'high_card'

hand_and_types_with_joker = {}
for hand in hands_and_bids.keys():
	hand_type = find_hand_type_with_joker(hand)
	hand_and_types_with_joker[hand] = hand_type

# print(hand_and_types_with_joker)

hand_rankings, total_winnings = calculate_total_winnings(hand_and_types_with_joker, hands_and_bids, card_rankings_with_joker)
# print('Sorted Rankings Part 2:', sorted(hand_rankings.items(), key=lambda x:x[1]))
print('Total Winnings Part 2:', total_winnings)
			
