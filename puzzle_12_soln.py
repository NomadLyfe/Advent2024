# Read and process input
with open("puzzle_11-12_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")

max_row = len(rows)
max_col = len(rows[0])

# Directions in clockwise order: UP, RIGHT, DOWN, LEFT
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Find guard's initial position
guard_row_start, guard_col_start = None, None
for r, row in enumerate(rows):
    for c, char in enumerate(row):
        if char == "^":
            guard_row_start, guard_col_start = r, c
            break

guard_row, guard_col = guard_row_start, guard_col_start

posits_visited = set()
guard_direction = 0  # Initial direction (UP)

# Move guard
def move_guard(r, c, direction, nor, noc):
    dr, dc = directions[direction]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < max_row and 0 <= nc < max_col):
        return None, None, None
    elif rows[nr][nc] == "#" or (nr == nor and nc == noc):
        return r, c, (direction + 1) % 4  # Turn clockwise
    else:
        return nr, nc, direction  # Move forward
    
new_obstacles = []
for new_obj_r in range(max_row):
    for new_obj_c in range(max_col):
        seen_points = set()
        guard_row, guard_col, guard_direction = guard_row_start, guard_col_start, 0
        while guard_row and guard_col and guard_direction != None:
            if (guard_row, guard_col, guard_direction) in seen_points:
                print(guard_row, guard_col)
                new_obstacles.append((guard_row, guard_col))
                break
            seen_points.add((guard_row, guard_col, guard_direction))
            guard_row, guard_col, guard_direction = move_guard(guard_row, guard_col, guard_direction, new_obj_r, new_obj_c)

print(len(new_obstacles))