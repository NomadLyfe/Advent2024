# Read and process input
with open("puzzle_19-20_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")
    grid = [[int(c) for c in row] for row in rows]
trailheads = []
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if height == 0:
            trailheads.append((x, y))
p1 = 0
for trailhead in trailheads:
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UP, DN, LT, RT
    curr_position = trailhead
    curr_value = grid[curr_position[1]][curr_position[0]]
    next_positions = [
        [
            (a + c, b + d)
            for (a, b), (c, d) in zip(directions, [(curr_position)] * 4)
            if 0 <= a + c < len(grid[0])
            and 0 <= b + d < len(grid)
            and grid[b + d][a + c] == curr_value + 1
        ]
    ]
    next_values = [[grid[pos[1]][pos[0]] for pos in next_positions[0]]]
    for _ in range(8):
        next_positions.append([])
        next_values.append([])
    i = 0
    nines = set()
    while len(next_values[i]) > 0:
        i += 1
        if i == 9:
            p1 += len(set(next_positions[-1]))
            break
        for dir in next_positions[i - 1]:
            curr_position = dir
            curr_value = grid[curr_position[1]][curr_position[0]]
            next_positions[i] += [
                (a + c, b + d)
                for (a, b), (c, d) in zip(directions, [(curr_position)] * 4)
                if 0 <= a + c < len(grid[0])
                and 0 <= b + d < len(grid)
                and grid[b + d][a + c] == curr_value + 1
            ]
            next_values[i] += [grid[pos[1]][pos[0]] for pos in next_positions[i]]
print(p1)
