# Read and process input
with open("puzzle_25-26_input.txt", "r") as file:
    input_data_rows = file.read().strip().split("\n\n")
games = [
    {g.split(": ")[0]: g.split(": ")[1].split(", ") for g in game.split("\n")}
    for game in input_data_rows
]
print(games)
