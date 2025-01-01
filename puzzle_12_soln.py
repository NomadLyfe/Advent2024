# from operator import sub, floordiv, add

# def check_then_floordiv (x, y):
#     if x != 0:
#         return floordiv(x, y) if x > 0 else -floordiv(x, y)
#     else:
#         return 0

# with open("puzzle_11-12_input.txt", "r") as file:
#     input = file.read()
#     rows = input.split("\n")
#     rows.pop()
#     max_row = len(rows)
#     max_col = len(rows[0])

#     # Directions in clockwise order: UP, RIGHT, DOWN, LEFT
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#     # Find guard's initial position
#     guard_row, guard_col = None, None
#     for r, row in enumerate(rows):
#         for c, char in enumerate(row):
#             if char == "^":
#                 guard_row, guard_col = r, c
#                 break

#     posits_visited = [(guard_row, guard_col)]
#     guard_direction = 0  # Initial direction (UP)

#     # Simulate guard movement
#     def move_guard(r, c, direction):
#         dr, dc = directions[direction]
#         nr, nc = r + dr, c + dc
#         if rows[nr][nc] != "#":
#             return nr, nc, direction  # Move forward
#         else:
#             return r, c, (direction + 1) % 4  # Turn clockwise

#     # Simulate guard path
#     turning_points = []  # Ordered list of turning points

#     while 0 < guard_row < max_row-1 and 0 < guard_col < max_col-1:
#         prev_row, prev_col, prev_direction = guard_row, guard_col, guard_direction
#         guard_row, guard_col, guard_direction = move_guard(
#             guard_row, guard_col, guard_direction
#         )

#         # Record positions visited
#         if guard_direction == prev_direction:
#             posits_visited.append((guard_row, guard_col))

#         # Record turning points
#         if guard_direction != prev_direction:
#             turning_points.append((prev_row, prev_col))
#     print(turning_points)
#     print(len(turning_points))
#     # Find potential obstacles
#     potential_obstacles = list()
#     for i in range(len(turning_points)-2):
#         p1 = turning_points[i]
#         p2 = turning_points[i + 1]
#         p3 = turning_points[i + 2]

#         # Check if p1, p2, and p3 form three corners of a rectangle
#         if (p1[0] == p2[0] and p2[1] == p3[1]) or (p1[1] == p2[1] and p2[0] == p3[0]):
#             # Calculate the fourth turning corner
#             p4 = (p3[0], p1[1]) if p1[0] == p2[0] else (p1[0], p3[1])

#             # Ensure p4 is within bounds and not an obstacle
#             if (
#                 0 < p4[0] < max_row-1
#                 and 0 < p4[1] < max_col-1
#                 and rows[p4[0]][p4[1]] != "#"
#                 and p4 in posits_visited
#             ):
#                 # Verify no other obstacles disrupt the loop
#                 clear_path = True
#                 for path in [
#                     ((p3[0], p3[1]), (p4[0], p4[1])),
#                     ((p4[0], p4[1]), (p1[0], p1[1])),
#                 ]:
#                     r1, c1 = path[0]
#                     r2, c2 = path[1]
#                     if r1 == r2:  # Horizontal path
#                         for c in range(min(c1, c2), max(c1, c2) + 1):
#                             if rows[r1][c] == "#":
#                                 clear_path = False
#                                 break
#                     elif c1 == c2:  # Vertical path
#                         for r in range(min(r1, r2), max(r1, r2) + 1):
#                             if rows[r][c1] == "#":
#                                 clear_path = False
#                                 break
#                     if not clear_path:
#                         break
#                 if clear_path:
#                     diff = tuple(map(sub, p4, p3))
#                     direc = tuple(map(check_then_floordiv, diff, diff))
#                     p4_obs = tuple(map(add, p4, direc))
#                     if p4_obs not in potential_obstacles and rows[p4_obs[0]][p4_obs[1]] != "#":
#                         potential_obstacles.append(p4_obs)

#     print(f"Potential obstacles: {potential_obstacles}")
#     print(f"Total: {len(potential_obstacles)}")

# advent_of_code_2024_day6_part2.py

# Read and process input
# with open("puzzle_11-12_input.txt", "r") as file:
#     input_data = file.read().strip()
#     rows = input_data.split("\n")

# max_row = len(rows)
# max_col = len(rows[0])

# # Directions in clockwise order: UP, RIGHT, DOWN, LEFT
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# # Find guard's initial position
# guard_row, guard_col = None, None
# for r, row in enumerate(rows):
#     for c, char in enumerate(row):
#         if char == "^":
#             guard_row, guard_col = r, c
#             break

# posits_visited = [(guard_row, guard_col)]
# guard_direction = 0  # Initial direction (UP)

# # Move guard
# def move_guard(r, c, direction):
#     dr, dc = directions[direction]
#     nr, nc = r + dr, c + dc
#     if 0 <= nr < max_row and 0 <= nc < max_col and rows[nr][nc] != "#":
#         return nr, nc, direction  # Move forward
#     else:
#         return r, c, (direction + 1) % 4  # Turn clockwise

# # Simulate guard path
# turning_points = []  # Ordered list of turning points
# while 0 < guard_row < max_row - 1 and 0 < guard_col < max_col - 1:
#     prev_row, prev_col, prev_direction = guard_row, guard_col, guard_direction
#     guard_row, guard_col, guard_direction = move_guard(guard_row, guard_col, guard_direction)

#     # Record turning points
#     if guard_direction != prev_direction:
#         turning_points.append((prev_row, prev_col))
#     else:
#         posits_visited.append((guard_row, guard_col))

# # Identify rectangles and obstacles
# potential_obstacles = []
# for i in range(len(turning_points) - 2):
#     p1 = turning_points[i]
#     p2 = turning_points[i + 1]
#     p3 = turning_points[i + 2]

#     # Check if p1, p2, and p3 form three corners of a rectangle
#     if (p1[0] == p2[0] and p2[1] == p3[1]) or (p1[1] == p2[1] and p2[0] == p3[0]):
#         # Calculate the fourth corner
#         p4 = (p3[0], p1[1]) if p1[0] == p2[0] else (p1[0], p3[1])

#         # Ensure p4 is within bounds and valid
#         if 0 <= p4[0] < max_row and 0 <= p4[1] < max_col:
#             if rows[p4[0]][p4[1]] != "#" and p4 in posits_visited:
#                 # Check for obstacles on edges
#                 clear_path = all(
#                     rows[r][c] != "#"
#                     for r, c in [(p3[0], p4[1]), (p4[0], p1[1])]
#                 )
#                 if clear_path:
#                     potential_obstacles.append(p4)

# print(f"Potential obstacles: {potential_obstacles}")
# print(f"Total: {len(potential_obstacles)}")

# advent_of_code_2024_day6_part2.py

# Read and process input
with open("puzzle_11-12_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")

max_row = len(rows)
max_col = len(rows[0])

# Directions in clockwise order: UP, RIGHT, DOWN, LEFT
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Find guard's initial position
guard_row, guard_col = None, None
for r, row in enumerate(rows):
    for c, char in enumerate(row):
        if char == "^":
            guard_row, guard_col = r, c
            break

posits_visited = set([(guard_row, guard_col)])
guard_direction = 0  # Initial direction (UP)

# Move guard
def move_guard(r, c, direction):
    dr, dc = directions[direction]
    nr, nc = r + dr, c + dc
    if 0 <= nr < max_row and 0 <= nc < max_col and rows[nr][nc] != "#":
        return nr, nc, direction  # Move forward
    else:
        return r, c, (direction + 1) % 4  # Turn clockwise

# Simulate guard path
turning_points = []  # Ordered list of turning points
while 0 < guard_row < max_row - 1 and 0 < guard_col < max_col - 1:
    prev_row, prev_col, prev_direction = guard_row, guard_col, guard_direction
    guard_row, guard_col, guard_direction = move_guard(guard_row, guard_col, guard_direction)

    # Record turning points
    if guard_direction != prev_direction:
        turning_points.append((prev_row, prev_col))
    posits_visited.add((guard_row, guard_col))

# Identify rectangles and obstacles
potential_obstacles = set()
for i in range(len(turning_points) - 2):
    p1 = turning_points[i]
    p2 = turning_points[i + 1]
    p3 = turning_points[i + 2]

    # Check if p1, p2, and p3 form three corners of a rectangle
    if (p1[0] == p2[0] and p2[1] == p3[1]) or (p1[1] == p2[1] and p2[0] == p3[0]):
        # Calculate the fourth corner
        p4 = (p3[0], p1[1]) if p1[0] == p2[0] else (p1[0], p3[1])

        # Ensure p4 is within bounds and valid
        if 0 <= p4[0] < max_row and 0 <= p4[1] < max_col:
            if rows[p4[0]][p4[1]] != "#" and p4 in posits_visited:
                # Check all edges of the rectangle
                rectangle_edges = [
                    ((p1[0], p1[1]), (p2[0], p2[1])),
                    ((p2[0], p2[1]), (p3[0], p3[1])),
                    ((p3[0], p3[1]), (p4[0], p4[1])),
                    ((p4[0], p4[1]), (p1[0], p1[1])),
                ]
                clear_path = True
                for edge in rectangle_edges:
                    (r1, c1), (r2, c2) = edge
                    if r1 == r2:  # Horizontal edge
                        for c in range(min(c1, c2), max(c1, c2) + 1):
                            if rows[r1][c] == "#":
                                clear_path = False
                                break
                    elif c1 == c2:  # Vertical edge
                        for r in range(min(r1, r2), max(r1, r2) + 1):
                            if rows[r][c1] == "#":
                                clear_path = False
                                break
                    if not clear_path:
                        break
                if clear_path:
                    potential_obstacles.add(p4)

print(f"Potential obstacles: {sorted(potential_obstacles)}")
print(f"Total: {len(potential_obstacles)}")
