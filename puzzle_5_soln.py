import re

with open("puzzle_5-6_input.txt", "r") as file:
    input = file.read()
    correct_functions = re.findall("mul\([0-9]*,[0-9]*\)", input)
    output = []
    for func in correct_functions:
        a, b = func.split("(")[1][:-1].split(",")
        output.append(int(a) * int(b))
print(sum(output))
