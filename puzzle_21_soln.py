# Read and process input
with open("puzzle_21-22_input.txt", "r") as file:
    input_data = file.read().strip()
stones = input_data.split(" ")

for _ in range(25):
    for i, stone in enumerate(stones):
        if stone == "0":
            stones[i] = "1"
        elif len(stone) % 2 == 0:
            stones[i] = (
                str(int(stone[: len(stone) // 2])),
                str(int(stone[len(stone) // 2 :])),
            )
        else:
            stones[i] = str(int(stone) * 2024)
    stones = [
        s for stone in stones for s in (stone if isinstance(stone, tuple) else [stone])
    ]
print(len(stones))
