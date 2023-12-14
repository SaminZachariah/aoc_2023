import re
import math
from collections import Counter
from functools import cmp_to_key

# input_file = "sample_inputs/D7_sample_input.txt"
input_file = "full_inputs/D7_full_input.txt"

card_strengths = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hands = []
with open(input_file, "r") as f:
    for line in f:
        hand, bid = line.split()
        hands.append([list(hand), bid])


def hand_type(hand):
    """Determines type of hand and return integer in [1,7]"""
    counts = list(Counter(hand).values())
    joker_count = Counter(hand).get("J", 0)
    print(joker_count)

    if joker_count == 4:
        return 7  # 4 Jokers makes 5 of a kind

    if joker_count == 3:
        if 2 in counts:
            return 7  # 3 Jokers and a pair makes 5 of a kind
        else:
            return 6  # 3 Jokers and no pair makes 4 of a kind

    if joker_count == 2:
        if 3 in counts:
            return 7  # 2 Jokers and a 3 of a kind makes 5 of a kind
        elif 2 == counts.count(2):
            return 6  # 2 Jokers and a pair makes 4 of a kind
        else:
            return 4  # 2 Jokers and no pair makes 3 of a kind

    if joker_count == 1:
        if 4 in counts:
            return 7  # 1 Joker and a 4 of a kind makes 5 of a kind
        elif 3 in counts:
            return 6  # 1 Joker and a 3 of a kind makes 4 of a kind
        elif 2 == counts.count(2):
            return 5  # 1 Joker and 2 pairs makes a full house
        elif 2 in counts:
            return 4  # 1 Joker and a pair makes 3 of a kind
        else:
            return 2  # 1 Joker and no pair makes 2 of a kind

    else:
        if 5 in counts:
            return 7  # No Jokers and a 5 of a kind makes 5 of a kind
        elif 4 in counts:
            return 6  # No Jokers and a 4 of a kind makes 4 of a kind
        elif 3 in counts and 2 in counts:
            return 5  # No Jokers and a 3 of a kind and a pair makes a full house
        elif 3 in counts:
            return 4  # No Jokers and a 3 of a kind makes 3 of a kind
        elif 2 == counts.count(2):
            return 3  # No Jokers and 2 pairs makes 2 pairs
        elif 2 in counts:
            return 2  # No Jokers and a pair makes 1 pair
        else:
            return 1  # No Jokers and no pair makes a high card


for hand in hands:
    hand.append(hand_type(hand[0]))


def compare_cards(card_1, card_2):
    if card_strengths[card_1] > card_strengths[card_2]:
        return 1
    elif card_strengths[card_1] < card_strengths[card_2]:
        return -1
    else:
        return 0


def compare_hands(h_1, h_2):
    """Return 1 if hand_1 > hand_2, -1 if hand_1 < hand_2, 0 if equal"""
    cards_1, type_1 = h_1[0], h_1[2]
    cards_2, type_2 = h_2[0], h_2[2]

    if type_1 > type_2:
        return 1
    elif type_1 < type_2:
        return -1
    else:
        if compare_cards(cards_1[0], cards_2[0]) != 0:
            return compare_cards(cards_1[0], cards_2[0])
        elif compare_cards(cards_1[1], cards_2[1]) != 0:
            return compare_cards(cards_1[1], cards_2[1])
        elif compare_cards(cards_1[2], cards_2[2]) != 0:
            return compare_cards(cards_1[2], cards_2[2])
        elif compare_cards(cards_1[3], cards_2[3]) != 0:
            return compare_cards(cards_1[3], cards_2[3])
        elif compare_cards(cards_1[4], cards_2[4]) != 0:
            return compare_cards(cards_1[4], cards_2[4])
        else:
            return 0


ranked_hands = sorted(hands, key=cmp_to_key(compare_hands))

winnings = []
for i, hand in enumerate(ranked_hands):
    winnings.append((i + 1) * int(hand[1]))

print(sum(winnings))
