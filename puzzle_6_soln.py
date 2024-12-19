import re

with open("puzzle_5-6_input.txt", "r") as file:
    input = file.read()
    correct_functions = re.findall("(mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\))", input)
    output = []
    is_enabled = True
    for func in correct_functions:
        if func == "do()":
            is_enabled = True
        elif func == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                a, b = func.split("(")[1][:-1].split(",")
                output.append(int(a) * int(b))
print(sum(output))