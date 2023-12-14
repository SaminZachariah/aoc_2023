import re
import math

# input_path = "sample_inputs/D3_sample_input.txt"
input_path = "full_inputs/D3_full_input.txt"

board = []

with open(input_path, "r") as f:
    for line in f:
        board.append(line.strip())

print(board)
print(len(board))
print(len(board[0]))

symbols = {
    (r, c): []
    for r in range(len(board))
    for c in range(len(board[0]))
    if board[r][c] not in ".0123456789"
}

for r, row in enumerate(board):
    for num in re.finditer(r"\d+", row):
        mask = {
            (r, c)
            for r in (r - 1, r, r + 1)
            for c in range(num.start() - 1, num.end() + 1)
        }

        for pos in mask & symbols.keys():
            print(pos, num.group())
            symbols[pos].append(int(num.group()))

# part 1
print(sum(sum(p) for p in symbols.values()))
# part 2
print(sum(math.prod(p) for p in symbols.values() if len(p) == 2))
