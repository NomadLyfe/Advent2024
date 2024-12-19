
with open("puzzle_1-2_input.txt", "r") as file:
    input = file.read().split("\n")
    input.pop()
    list_1 = sorted([int(el.split("   ")[0]) for el in input])
    list_2 = sorted([int(el.split("   ")[1]) for el in input])
    combined = [abs(a - b) for a, b in zip(list_1, list_2)]

print(sum(combined))