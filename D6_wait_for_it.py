import re
import math

# input = "sample_inputs/D6_sample_input.txt"
input = "full_inputs/D6_full_input.txt"

races = []
with open(input, "r") as f:
    times = f.readline().split(":")[1].strip().split()
    distances = f.readline().split(":")[1].strip().split()
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]

    races = list(zip(times, distances))


# part 2
races = [(61709066, 643118413621041)]

ways_to_win = []

for r, race in enumerate(races):
    t = race[0]
    d = race[1]

    winning_hold_times = []

    for i in range(t):
        if i % 10 == 0:
            print(i / t)
        hold_time = i
        run_time = t - i
        dist = run_time * hold_time

        if dist > d:
            winning_hold_times.append(hold_time)

    ways_to_win.append(winning_hold_times)


print(math.prod(len(wins) for wins in ways_to_win))
