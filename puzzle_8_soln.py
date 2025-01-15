with open("puzzle_7-8_input.txt", "r") as file:
    input = file.read()
    rows = input.split("\n")
    rows.pop()
    out = []
    for row_idx, row in enumerate(rows):
        for col_idx, char in enumerate(row):
            if (
                char == "A"
                and 0 < row_idx < len(rows) - 1
                and 0 < col_idx < len(row) - 1
            ):
                if (
                    rows[row_idx - 1][col_idx - 1] == "M"
                    and rows[row_idx - 1][col_idx + 1] == "M"
                    and rows[row_idx + 1][col_idx - 1] == "S"
                    and rows[row_idx + 1][col_idx + 1] == "S"
                ):
                    out.append((col_idx, row_idx))
                elif (
                    rows[row_idx - 1][col_idx - 1] == "M"
                    and rows[row_idx - 1][col_idx + 1] == "S"
                    and rows[row_idx + 1][col_idx - 1] == "M"
                    and rows[row_idx + 1][col_idx + 1] == "S"
                ):
                    out.append((col_idx, row_idx))
                elif (
                    rows[row_idx - 1][col_idx - 1] == "S"
                    and rows[row_idx - 1][col_idx + 1] == "S"
                    and rows[row_idx + 1][col_idx - 1] == "M"
                    and rows[row_idx + 1][col_idx + 1] == "M"
                ):
                    out.append((col_idx, row_idx))
                elif (
                    rows[row_idx - 1][col_idx - 1] == "S"
                    and rows[row_idx - 1][col_idx + 1] == "M"
                    and rows[row_idx + 1][col_idx - 1] == "S"
                    and rows[row_idx + 1][col_idx + 1] == "M"
                ):
                    out.append((col_idx, row_idx))

    print(len(out))
