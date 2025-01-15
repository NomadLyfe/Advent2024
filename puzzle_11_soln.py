with open("puzzle_11-12_input.txt", "r") as file:
    input = file.read()
    rows = input.split("\n")
    rows.pop()
    max_row = len(rows) - 1
    max_col = len(rows[0]) - 1
    guard_direction = "UP"
    guard_row, guard_col = None, None
    posits_visited = set()
    for row_i, row in enumerate(rows):
        for col_i, char in enumerate(row):
            if char == "^":
                guard_row, guard_col = row_i, col_i
    posits_visited.add((guard_row, guard_col))

    def move_guard(direction):
        global guard_row, guard_col, guard_direction, posits_visited
        if direction == "UP":
            if rows[guard_row - 1][guard_col] != "#":
                guard_row -= 1
                posits_visited.add((guard_row, guard_col))
            else:
                guard_direction = "RT"
        elif direction == "RT":
            if rows[guard_row][guard_col + 1] != "#":
                guard_col += 1
                posits_visited.add((guard_row, guard_col))
            else:
                guard_direction = "DN"
        elif direction == "DN":
            if rows[guard_row + 1][guard_col] != "#":
                guard_row += 1
                posits_visited.add((guard_row, guard_col))
            else:
                guard_direction = "LT"
        elif direction == "LT":
            if rows[guard_row][guard_col - 1] != "#":
                guard_col -= 1
                posits_visited.add((guard_row, guard_col))
            else:
                guard_direction = "UP"

    while (
        guard_row != 0
        and guard_col != 0
        and guard_row != max_row
        and guard_col != max_col
    ):
        move_guard(guard_direction)
    print(len(posits_visited))
