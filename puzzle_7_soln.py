with open("puzzle_7-8_input.txt", "r") as file:
    input = file.read()
    rows = input.split("\n")
    rows.pop()
    out = []
    for row_idx, row in enumerate(rows):
        for col_idx, char in enumerate(row):
            if char == "X":
                def in_bounds(r, c):
                    return 0 <= r < len(rows) and 0 <= c < len(row)
                if in_bounds(row_idx - 3, col_idx - 3) and \
                   rows[row_idx - 1][col_idx - 1] == "M" and \
                   rows[row_idx - 2][col_idx - 2] == "A" and \
                   rows[row_idx - 3][col_idx - 3] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx - 3, col_idx) and \
                   rows[row_idx - 1][col_idx] == "M" and \
                   rows[row_idx - 2][col_idx] == "A" and \
                   rows[row_idx - 3][col_idx] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx - 3, col_idx + 3) and \
                   rows[row_idx - 1][col_idx + 1] == "M" and \
                   rows[row_idx - 2][col_idx + 2] == "A" and \
                   rows[row_idx - 3][col_idx + 3] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx, col_idx - 3) and \
                   rows[row_idx][col_idx - 1] == "M" and \
                   rows[row_idx][col_idx - 2] == "A" and \
                   rows[row_idx][col_idx - 3] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx, col_idx + 3) and \
                   rows[row_idx][col_idx + 1] == "M" and \
                   rows[row_idx][col_idx + 2] == "A" and \
                   rows[row_idx][col_idx + 3] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx + 3, col_idx - 3) and \
                   rows[row_idx + 1][col_idx - 1] == "M" and \
                   rows[row_idx + 2][col_idx - 2] == "A" and \
                   rows[row_idx + 3][col_idx - 3] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx + 3, col_idx) and \
                   rows[row_idx + 1][col_idx] == "M" and \
                   rows[row_idx + 2][col_idx] == "A" and \
                   rows[row_idx + 3][col_idx] == "S":
                    out.append((col_idx, row_idx))
                if in_bounds(row_idx + 3, col_idx + 3) and \
                   rows[row_idx + 1][col_idx + 1] == "M" and \
                   rows[row_idx + 2][col_idx + 2] == "A" and \
                   rows[row_idx + 3][col_idx + 3] == "S":
                    out.append((col_idx, row_idx))

    print(len(out))