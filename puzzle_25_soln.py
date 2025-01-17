# Read and process input
with open("puzzle_25-26_input.txt", "r") as file:
    input_data_rows = file.read().strip().split("\n\n")
games = [
    {
        g.split(": ")[0]: [int(i[2:]) for i in g.split(": ")[1].split(", ")]
        for g in game.split("\n")
    }
    for game in input_data_rows
]


def solve_claw_machines(games):
    prizes_won = 0
    total_tokens = 0

    for game in games:
        # Extract game parameters
        ax, ay = game["Button A"]
        bx, by = game["Button B"]
        px, py = game["Prize"]

        found_solution = False
        min_cost = float("inf")

        # Try all possible values of a (button A presses)
        for a in range(101):  # Up to 100 presses for A
            # Calculate the remainder of x and y after pressing A
            x_remaining = px - a * ax
            y_remaining = py - a * ay

            # Check if b (button B presses) is valid
            if x_remaining % bx == 0 and y_remaining % by == 0:
                b_x = x_remaining // bx
                b_y = y_remaining // by

                if b_x == b_y and b_x >= 0:  # Both equations must yield the same b
                    cost = 3 * a + b_x
                    if cost < min_cost:
                        min_cost = cost
                        found_solution = True

        if found_solution:
            prizes_won += 1
            total_tokens += min_cost

    return prizes_won, total_tokens


# Solve the problem
prizes, tokens = solve_claw_machines(games)
print(f"Prizes won: {prizes}, Total tokens: {tokens}")
