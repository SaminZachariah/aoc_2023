import re

# input_path = "sample_inputs/D2_sample_input.txt"
input_path = "full_inputs/D2_full_input.txt"

# Part 2
with open(input_path, "r") as f:
    # Format text into a dictionary of games
    # games[game_id] = [round_1, round_2, ... round_n]
    # round_i = {"red": R, "green": G, "blue": B}
    games = {}
    for game in f:
        game = game.rstrip()
        game_id = game.split(":")[0][
            5:
        ]  # Split on the colon, take the first element, and remove the "Game " prefix
        # print(f"Game: {game_id}")

        game_id = int(game_id)

        games[game_id] = []

        rounds = (
            game.split(":")[1].lstrip().split("; ")
        )  # Rounds have format "X blue, Y red, Z green"

        for round in rounds:
            cubes = round.split(",")

            round_color_count = {"red": 0, "green": 0, "blue": 0}
            for cube in cubes:
                color = cube.split()[1]
                count = int(cube.split()[0])
                if "blue" in color:
                    round_color_count["blue"] = count
                if "red" in color:
                    round_color_count["red"] = count
                if "green" in color:
                    round_color_count["green"] = count

            games[game_id].append(round_color_count)

    # Iterate over games to compute feasibility / game power
    possible_game_ids = []  # list of game ids that are possible for part 1
    bag_cube_counts = {"red": 12, "green": 13, "blue": 14}  # fixed values for part 1
    game_powers = []  # powers of each game for part 2

    for game, rounds in games.items():
        possible_game = True

        red_min = 0
        green_min = 0
        blue_min = 0

        for round in rounds:
            # part 1, discard games that are impossible
            if round["red"] > bag_cube_counts["red"]:
                possible_game = False
            if round["green"] > bag_cube_counts["green"]:
                possible_game = False
            if round["blue"] > bag_cube_counts["blue"]:
                possible_game = False

            # part 2, find minimum bag for a valid game
            red_min = max(red_min, round["red"])
            green_min = max(green_min, round["green"])
            blue_min = max(blue_min, round["blue"])

        power = red_min * green_min * blue_min
        game_powers.append(power)

        if possible_game:
            possible_game_ids.append(game)

    print(sum(possible_game_ids))
    print(sum(game_powers))
