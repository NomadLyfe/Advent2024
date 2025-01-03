# Read and process input
with open("puzzle_15-16_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")
antinodes = set()
for y, row in enumerate(rows):
    for x, symbol in enumerate(row):
        if symbol != ".":
            for j, r in enumerate(rows):
                for i, s in enumerate(r):
                    if s == symbol and i != x and j != y:
                        dx = i-x
                        dy = j-y
                        if 0 <= x-dx < len(rows[0]) and 0 <= y-dy < len(rows):
                            antinodes.add((x-dx, y-dy))
                        if 0 <= i+dx < len(rows[0]) and 0 <= j+dy < len(rows):
                            antinodes.add((i+dx, j+dy))
print(len(antinodes))