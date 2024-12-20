# with open("puzzle_11-12_input.txt", "r") as file:
#     input = file.read()
#     rows = input.split("\n")
#     rows.pop()
#     max_row = len(rows) - 1
#     max_col = len(rows[0]) - 1
#     guard_direction = "UP"
#     guard_row, guard_col = None, None
#     posits_visited = []
#     for row_i, row in enumerate(rows):
#         for col_i, char in enumerate(row):
#             if char == "^":
#                 guard_row, guard_col = row_i, col_i
#     posits_visited.append((guard_row, guard_col))
#     def move_guard(direction):
#         global guard_row, guard_col, guard_direction, posits_visited
#         if direction == "UP":
#             if rows[guard_row - 1][guard_col] != "#":
#                 guard_row -= 1
#                 posits_visited.append((guard_row, guard_col))
#             else:
#                 guard_direction = "RT"
#         elif direction == "RT":
#             if rows[guard_row][guard_col + 1] != "#":
#                 guard_col += 1
#                 posits_visited.append((guard_row, guard_col))
#             else:
#                 guard_direction = "DN"
#         elif direction == "DN":
#             if rows[guard_row + 1][guard_col] != "#":
#                 guard_row += 1
#                 posits_visited.append((guard_row, guard_col))
#             else:
#                 guard_direction = "LT"
#         elif direction == "LT":
#             if rows[guard_row][guard_col - 1] != "#":
#                 guard_col -= 1
#                 posits_visited.append((guard_row, guard_col))
#             else:
#                 guard_direction = "UP"
#     while guard_row != 0 and guard_col != 0 and guard_row != max_row and guard_col != max_col:
#         move_guard(guard_direction)
#     turning_points = []
#     for i in range(1, len(posits_visited) - 1):
#         prev_pos = posits_visited[i - 1]
#         curr_pos = posits_visited[i]
#         next_pos = posits_visited[i + 1]

#         curr_direction = (curr_pos[0] - prev_pos[0], curr_pos[1] - prev_pos[1])
#         next_direction = (next_pos[0] - curr_pos[0], next_pos[1] - curr_pos[1])

#         if curr_direction != next_direction:
#             dirr = "UP" if next_direction == (-1, 0) else ("RT" if next_direction == (0, 1) else ("DN" if next_direction == (1, 0) else ("LT")))
#             turning_points.append((curr_pos, dirr))
#     print(turning_points)
#     def in_bounds(r, c):
#         return 0 <= r <= max_row and 0 <= c <= max_col
#     potential_obstacles = []
#     for i, data in enumerate(turning_points[3:]):
#         d = data[1]
#         three_prev_turn = turning_points[i][0]
#         two_prev_turn = turning_points[i+1][0]
#         prev_turn = turning_points[i+2][0]
#         curr_turn = turning_points[i+3][0]
#         if three_prev_turn[0] == two_prev_turn[0] and two_prev_turn[1] == prev_turn[1] and prev_turn[0] == curr_turn[0]:
#             if d == "UP" and curr_turn[1] < three_prev_turn[1]:
#                 no_obs = True
#                 for j in range(curr_turn[0], three_prev_turn[0], -1):
#                     if rows[j][three_prev_turn[1]] == "#":
#                         no_obs = False
#                         break
#                 if no_obs:
#                     potential_obstacles.append((curr_turn[0], three_prev_turn[1]-1))
#             elif d == "DN" and curr_turn[1] > three_prev_turn[1]:
#                 no_obs = True
#                 for j in range(curr_turn[0], three_prev_turn[0]):
#                     if rows[j][three_prev_turn[1]] == "#":
#                         no_obs = False
#                         break
#                 if no_obs:
#                     potential_obstacles.append((curr_turn[0], three_prev_turn[1]+1))
#         elif three_prev_turn[1] == two_prev_turn[1] and two_prev_turn[0] == prev_turn[0] and prev_turn[1] == curr_turn[1]:
#             if d == "RT" and curr_turn[0] < three_prev_turn[0]:
#                 no_obs = True
#                 for j in range(curr_turn[1], three_prev_turn[1]):
#                     if rows[three_prev_turn[0]][j] == "#":
#                         no_obs = False
#                         break
#                 if no_obs:
#                     potential_obstacles.append((three_prev_turn[0]-1, curr_turn[1]))
#             elif d == "LT" and curr_turn[0] > three_prev_turn[0]:
#                 no_obs = True
#                 for j in range(curr_turn[1], three_prev_turn[1], -1):
#                     if rows[three_prev_turn[0]][j] == "#":
#                         no_obs = False
#                         break
#                 if no_obs:
#                     potential_obstacles.append((three_prev_turn[0]+1, curr_turn[1]))
#     print(potential_obstacles)
#     print(len(potential_obstacles))

with open("puzzle_11-12_input.txt", "r") as file:
    input = file.read()
    rows = input.split("\n")
    rows.pop()
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

    posits_visited = [(guard_row, guard_col)]
    guard_direction = 0  # Initial direction (UP)

    # Simulate guard movement
    def move_guard(r, c, direction):
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc
        if 0 <= nr <= max_row-1 and 0 <= nc <= max_col-1 and rows[nr][nc] != "#":
            return nr, nc, direction  # Move forward
        else:
            return r, c, (direction + 1) % 4  # Turn clockwise

    # Simulate guard path
    turning_points = []  # Ordered list of turning points
    prev_direction = None

    while 0 < guard_row < max_row-1 and 0 < guard_col < max_col-1:
        prev_row, prev_col = guard_row, guard_col
        guard_row, guard_col, guard_direction = move_guard(
            guard_row, guard_col, guard_direction
        )
        posits_visited.append((guard_row, guard_col))

        # Record turning points
        if guard_direction != prev_direction:
            turning_points.append((prev_row, prev_col))
            prev_direction = guard_direction

    # Find potential obstacles
    potential_obstacles = set()

    for i in range(len(turning_points)-2):
        p1 = turning_points[i]
        p2 = turning_points[i + 1]
        p3 = turning_points[i + 2]

        # Check if p1, p2, and p3 form three corners of a rectangle
        if (p1[0] == p2[0] and p2[1] == p3[1]) or (p1[1] == p2[1] and p2[0] == p3[0]):
            # Calculate the fourth corner
            p4 = (p1[0], p3[1]) if p1[0] == p2[0] else (p3[0], p1[1])

            # Ensure p4 is within bounds and not an obstacle
            if (
                0 <= p4[0] < max_row
                and 0 <= p4[1] < max_col
                and rows[p4[0]][p4[1]] != "#"
                # and p4 not in posits_visited
            ):
                # Verify no other obstacles disrupt the loop
                clear_path = True
                for path in [
                    ((p1[0], p1[1]), (p2[0], p2[1])),
                    ((p2[0], p2[1]), (p3[0], p3[1])),
                    ((p3[0], p3[1]), (p4[0], p4[1])),
                    ((p4[0], p4[1]), (p1[0], p1[1])),
                ]:
                    r1, c1 = path[0]
                    r2, c2 = path[1]
                    if r1 == r2:  # Horizontal path
                        for c in range(min(c1, c2), max(c1, c2) + 1):
                            if rows[r1][c] == "#":
                                clear_path = False
                                break
                    elif c1 == c2:  # Vertical path
                        for r in range(min(r1, r2), max(r1, r2) + 1):
                            if rows[r][c1] == "#":
                                clear_path = False
                                break
                    if not clear_path:
                        break
                if clear_path:
                    potential_obstacles.add(p4)

    print(f"Potential obstacles: {potential_obstacles}")
    print(f"Total: {len(potential_obstacles)}")
