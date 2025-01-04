# Read and process input
with open("puzzle_17-18_input.txt", "r") as file:
    input_data = file.read().strip()
    modified_input = [(input_data[i], input_data[i+1]) if i != len(input_data)-1 else (input_data[i], None) for i in range(0, len(input_data), 2)]
memory = []
for i, (file, empty) in enumerate(modified_input):
    memory.append([str(i)] * int(file))
    if empty:
        memory.append(["."] * int(empty))
reversed_memory = memory[::-1]
for pos, val in enumerate(reversed_memory):
    # fwd_pos = len(memory) - 1 - pos
    if ("." not in val) and len(val) > 0:
        first_empty_viable_pos = None
        first_empty_pos = None
        for i, v in enumerate(reversed_memory[::-1]):
            if ("." in v) and len(v) >= len(val):
                first_empty_viable_pos = len(reversed_memory) - 1 - i
                break
        for i, v in enumerate(reversed_memory[::-1]):
            if ("." in v):
                first_empty_pos = len(reversed_memory) - 1 - i
                break
        if first_empty_pos and first_empty_pos <= pos:
            print(val)
            break
        if first_empty_viable_pos and first_empty_viable_pos > pos:
            if len(reversed_memory[first_empty_viable_pos]) == len(val):
                empties = reversed_memory[first_empty_viable_pos]
                reversed_memory[first_empty_viable_pos] = val
                reversed_memory[pos] = empties
            else:
                diff = len(reversed_memory[first_empty_viable_pos]) - len(val)
                reversed_memory[first_empty_viable_pos] = val
                reversed_memory.insert(first_empty_viable_pos, ['.'] * diff)
                reversed_memory[pos] = ['.'] * len(val)
flattenned_memory = []         
for l in reversed_memory[::-1]:
    flattenned_memory += l
p2 = 0
# print(flattenned_memory[:50892])
for i, el in enumerate(flattenned_memory):
    if el != ".":
        p2 += (i*int(el))
print(p2)