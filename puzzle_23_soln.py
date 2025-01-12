# Read and process input
with open("puzzle_23-24_input.txt", "r") as file:
    input_data_rows = file.read().strip().split('\n')
    data = [[char for char in row] for row in input_data_rows]

for d in data:
    print(d)