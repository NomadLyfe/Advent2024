import numpy as np
import itertools
# Read and process input
with open("puzzle_13-14_input.txt", "r") as file:
    input_data = file.read().strip()
    rows = input_data.split("\n")

equations = [(int(row.split(":")[0]), [int(x) for x in row.split(":")[1].strip().split(" ")]) for row in rows]
p2 = 0
operators = ["+", "*", "||"]
for test_val, vals in equations:
    if test_val == sum(vals):
        print(test_val, " = the sum of ", vals)
        p2 += test_val
    elif test_val == np.prod(vals):
        print(test_val, " = the product of ", vals)
        p2 += test_val
    else:
        permutations = list(list(itertools.product(operators, repeat=len(vals)-1)))
        for perm in permutations:
            tot = vals[0]
            for i, op in enumerate(perm):
                if op == "+":
                    tot += vals[i+1]
                    if tot > test_val:
                        break
                elif op == "*":
                    tot *= vals[i+1]
                    if tot > test_val:
                        break
                elif op == "||":
                    tot = int(f'{str(tot)}{str(vals[i+1])}')
                    if tot > test_val:
                        break
            if tot == test_val:
                print(test_val, " = the ", perm, " perm of ", vals)
                p2 += test_val
                break

print(p2)