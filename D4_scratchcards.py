# input_path = "sample_inputs/D4_sample_input.txt"
input_path = "full_inputs/D4_full_input.txt"

from collections import defaultdict

card_multiplicity = defaultdict(lambda: 1)
points = 0

with open(input_path, "r") as f:
    for line in f:
        card = int(line.split(":")[0].replace("Card", "").strip())

        curr_num = card_multiplicity[card]

        winning_nums, your_nums = line.split(":")[1].strip().split("|")
        winning_nums = winning_nums.split()
        your_nums = your_nums.split()

        shared_nums = len(set(winning_nums) & set(your_nums))

        to_copy = []
        if shared_nums > 0:
            # part 2
            to_copy = [i for i in range(card + 1, card + shared_nums + 1)]
            for c in to_copy:
                card_multiplicity[c] += curr_num

            # part 1
            points += 2 ** (shared_nums - 1)

        print(
            f"{curr_num} copies of card {card}. There are {shared_nums} matches, so copy {to_copy} each {curr_num} times"
        )


print(points)
print(sum(card_multiplicity.values()))
