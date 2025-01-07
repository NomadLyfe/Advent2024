# Read and process input
with open("puzzle_21-22_input.txt", "r") as file:
    input_data = file.read().strip().split(" ")

stones = [int(stone) for stone in input_data]

DP = {}

def solve(n, t):
    if (n, t) in DP:
        return DP[(n, t)]
    if t == 0:
        r = 1
    elif n == 0:
        r = solve(1, t-1)
    elif len(str(n)) % 2 == 0:
        left = int(str(n)[:len(str(n))//2])
        right = int(str(n)[len(str(n))//2:])
        r = solve(left, t-1) + solve(right, t-1)
    else:
        r = solve(2024*n, t-1)
    DP[(n, t)] = r
    return r

p2 = sum(solve(stone, 75) for stone in stones)

print(p2)