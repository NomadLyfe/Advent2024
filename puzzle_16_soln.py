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
                        antinodes.add((x, y))
                        antinodes.add((i, j))
                        dx = i-x
                        dy = j-y
                        up_y = y-dy
                        dn_y = j+dy
                        up_x = x-dx
                        dn_x = i+dx
                        in_graph = True
                        while in_graph:
                            if 0 <= up_x < len(rows[0]) and 0 <= up_y < len(rows):
                                antinodes.add((up_x, up_y))
                            if 0 <= dn_x < len(rows[0]) and 0 <= dn_y < len(rows):
                                antinodes.add((dn_x, dn_y))
                            if not (0 <= up_x < len(rows[0]) and 0 <= up_y < len(rows)) and not (0 <= dn_x < len(rows[0]) and 0 <= dn_y < len(rows)):
                                in_graph = False
                            up_y -= dy
                            dn_y += dy
                            up_x -= dx
                            dn_x += dx
print(len(antinodes))