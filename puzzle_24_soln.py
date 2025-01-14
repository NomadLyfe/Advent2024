# Read and process input
with open("puzzle_23-24_input.txt", "r") as file:
    input_data_rows = file.read().strip().split('\n')
    grid = [[char for char in row] for row in input_data_rows]

seen = set()
plants = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
regions = {}
p2 = 0

class Region():
    def __init__(self, x, y):
        self.plots = [(x, y)]
        self.area = 1
        self.horizontal_sides = set()  # Track unique horizontal fence lines
        self.vertical_sides = set()    # Track unique vertical fence lines
        seen.add((x, y))

    def treverse_tree(self, x, y, plot):
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                if grid[new_y][new_x] == plot:
                    if (new_x, new_y) not in seen:
                        seen.add((new_x, new_y))
                        self.area += 1
                        self.treverse_tree(new_x, new_y, plot)
                else:
                    # Add unique fence segments
                    if dx == 0:  # Vertical segment
                        self.vertical_sides.add((x, y, new_x, new_y))
                    if dy == 0:  # Horizontal segment
                        self.horizontal_sides.add((x, y, new_x, new_y))
            else:
                # Add outer boundary segments
                if dx == 0:  # Vertical segment
                    self.vertical_sides.add((x, y, x + dx, y + dy))
                if dy == 0:  # Horizontal segment
                    self.horizontal_sides.add((x, y, x + dx, y + dy))

    def _count_unique_sides(self, sides):
        # Filter out directly adjacent sides
        sorted_sides = sorted(sides)
        unique_sides = 0
        seen_sides = []
        print(sorted_sides)
        for side in (sorted_sides):
            if side not in seen_sides:
                unique_sides += 1
                seen_sides.append(side)
            for side_2 in (sorted_sides):
                if side != side_2 and (((side[0] == side_2[0]) and (side[2] == side_2[2]) and (abs(side[1] - side_2[1]) == 1)) or ((side[1] == side_2[1]) and side[3] == side_2[3] and (abs(side[0] - side_2[0]) == 1))):
                    seen_sides.append(side_2)
        return unique_sides

    def price(self):
        # Count unique horizontal and vertical sides
        unique_horizontals = self._count_unique_sides(self.horizontal_sides)
        unique_verticals = self._count_unique_sides(self.vertical_sides)
        print(unique_horizontals + unique_verticals)
        total_sides = unique_horizontals + unique_verticals
        return self.area * total_sides

# Initialize regions
for plant in plants:
    regions[plant] = []

# Traverse the grid
for y, row in enumerate(grid):
    for x, garden_plot in enumerate(row):
        if x == 0 and y == 0 and (x, y) not in seen:
            new_region = Region(x, y)
            new_region.treverse_tree(x, y, garden_plot)
            p2 += new_region.price()
            regions[garden_plot].append(new_region)
        break
    break

# Output the total price for Part 2
print(p2)
