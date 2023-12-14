import sys
import re


input_path = "full_inputs/D1_full_input.txt"

# Part 2
with open(input_path, "r") as f:
    # For each line in file, find the first and last number (digit or spelled out)
    # Sum the 2 digit numbers from each line
    string_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }

    calibration_values = []

    for line in f:
        digit_matches = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )

        first_digit = string_to_digit[digit_matches[0]]
        second_digit = string_to_digit[digit_matches[-1]]

        val = int(first_digit) * 10 + int(second_digit)

        calibration_values.append(val)

    print(sum(calibration_values))

pass

# Part 1
with open(input_path, "r") as f:
    # For each line in file find the first and last numeral in each line
    # Note that first and last numeral may be the same
    # Sum the 2 digit numbers from each line

    calibration_values = []

    for line in f:
        digit_matches = re.findall(r"\d", line)
        first_digit = int(digit_matches[0])
        second_digit = int(digit_matches[-1])

        calibration_values.append(first_digit * 10 + second_digit)

    print(sum(calibration_values))
