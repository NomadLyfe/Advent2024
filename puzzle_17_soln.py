# Read and process input
with open("puzzle_17-18_input.txt", "r") as file:
    input_data = file.read().strip()
    modified_input = [
        (
            (input_data[i], input_data[i + 1])
            if i != len(input_data) - 1
            else (input_data[i], None)
        )
        for i in range(0, len(input_data), 2)
    ]
memory = ""
for i, (file, empty) in enumerate(modified_input):
    memory += f" {str(i)} " * int(file)
    if empty:
        memory += " . " * int(empty)
memory_positions = memory.strip().split(" ")
memory_positions = [x for x in memory_positions if x != ""]
print(len(memory_positions))
reversed_memory_positions = memory_positions[::-1]
for pos, pos_val in enumerate(reversed_memory_positions):
    fwd_pos = len(memory_positions) - 1 - pos
    if (pos_val != ".") and ("." in memory_positions):
        first_empty_pos = memory_positions.index(".")
        if first_empty_pos >= fwd_pos:
            break
        memory_positions[first_empty_pos] = pos_val
        memory_positions[fwd_pos] = "."
print(memory_positions)
p1 = 0
for i, el in enumerate(memory_positions):
    if el != ".":
        p1 += i * int(el)
print(p1)
