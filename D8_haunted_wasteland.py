import re
from itertools import cycle
import math

# input_path = "./D8_sample_input.txt"
input_path = "./D8_full_input.txt"

instructions = ""
nodes = {}

with open(input_path, "r") as file:
    for line in file:
        if "\n" == line:
            pass
        elif re.match("^[LR]+$", line.strip()):
            instructions = line.strip()
            # print(f"instruction match {instructions}")
        else:
            m = re.findall(r"([A-Z]+)", line)
            # print(m)
            start, left, right = m
            nodes[start] = {"L": left, "R": right}


def traverse(instructions, nodes, start, end):
    current_node = start
    print(current_node)
    instruction_cycle = cycle(instructions)
    for c, direction in enumerate(instruction_cycle):
        print(f"count {c}, dir {direction}")
        if current_node == end:
            print(f"DONE in {c} steps")
            break
        else:
            current_node = nodes[current_node][direction]


traverse(instructions, nodes, "AAA", "ZZZ")


# Realized that directions are not repeated starting from final node,
# But rather you RESTART at the start node, and go through the directions again
def traverse_2(instructions, nodes):
    current_nodes = [node for node in nodes if node[2] == "A"]
    cycles = []
    for node in current_nodes:
        for steps, direction in enumerate(cycle(instructions), start=1):
            node = nodes[node][direction]
            if node[2] == "Z":
                cycles.append(steps)
                break

    return math.lcm(*cycles)


print(traverse_2(instructions, nodes))
