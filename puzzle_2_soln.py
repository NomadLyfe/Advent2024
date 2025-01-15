with open("puzzle_1-2_input.txt", "r") as file:
    input = file.read().split("\n")
    input.pop()
    list_1 = [int(el.split("   ")[0]) for el in input]
    set_1 = set(list_1)
    list_2 = [int(el.split("   ")[1]) for el in input]
    counter = {}
    for el in list_2:
        if counter.get(el):
            counter[el] += 1
        else:
            counter[el] = 1
    output = []
    for el in set_1:
        if counter.get(el):
            output.append(counter[el] * el)

print(sum(output))
