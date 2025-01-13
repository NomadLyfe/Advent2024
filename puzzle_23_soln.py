# Read and process input
with open("puzzle_23-24_input.txt", "r") as file:
    input_data_rows = file.read().strip().split('\n')
    grid = [[char for char in row] for row in input_data_rows]

seen = []
plants = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
regions = {}
p1 = 0

class Region():
    def __init__(self, x, y):
        self.plots = [(x, y)]
        self.perim = 4
        self.area = 1
        seen.append((x, y))

    def treverse_tree(self, x, y, plot):
        for new_x, new_y in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                num_same_neihbors = 0
                if grid[new_y][new_x] == plot:
                    if (new_x, new_y) not in seen:
                        seen.append((new_x, new_y))
                        self.area += 1
                        self.perim += 3
                        self.treverse_tree(new_x, new_y, plot)
                    elif (new_x, new_y) in seen:
                        num_same_neihbors += 1
                if num_same_neihbors > 0:
                    self.perim -= num_same_neihbors
    
    def price(self):
        return (self.area * self.perim)


for plant in plants:
    regions[plant] = []

for y, row in enumerate(grid):
    for x, garden_plot in enumerate(row):
        if (x, y) not in seen:
            new_region = Region(x, y)
            new_region.treverse_tree(x, y, garden_plot)
            p1 += new_region.price()
            regions[garden_plot].append(new_region)

# print([f'Plant K: area of {ob.area} and perimeter of {ob.perim}' for ob in regions['K']])
print(p1)