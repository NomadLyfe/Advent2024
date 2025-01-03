# Read and process input
with open("puzzle_13-14_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")

inp = [(int(row.split(":")[0]), [int(x) for x in row.split(":")[1].strip().split(" ")]) for row in rows]
print(inp)