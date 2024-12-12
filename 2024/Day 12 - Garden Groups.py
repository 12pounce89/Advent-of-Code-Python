'''
# Part 1

grid = []

with open('2024/data/day12.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

regions = []
allPos = []

def makeRegion(y, x, coords):
    coords.add((y, x))
    if y - 1 >= 0:
        if grid[y][x] == grid[y - 1][x] and (y - 1, x) not in coords:
            coords.union(makeRegion(y - 1, x, coords))
    if x - 1 >= 0:
        if grid[y][x] == grid[y][x - 1] and (y, x - 1) not in coords:
            coords.union(makeRegion(y, x - 1, coords))
    if y + 1 < len(grid):
        if grid[y][x] == grid[y + 1][x] and (y + 1, x) not in coords:
            coords.union(makeRegion(y + 1, x, coords))
    if x + 1 < len(grid[0]):
        if grid[y][x] == grid[y][x + 1] and (y, x + 1) not in coords:
            coords.union(makeRegion(y, x + 1, coords))
    return coords

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in allPos:
            new = makeRegion(i, j, set())
            regions.append(sorted(list(new)))
            allPos.extend(list(new))

price = 0

for region in regions:
    perimeter = len(region) * 4
    checked = set()
    for coord in region:
        checked.add(coord)
        if coord[0] - 1 >= 0:
            if (coord[0] - 1, coord[1]) in region and (coord[0] - 1, coord[1]) not in checked:
                perimeter -= 2
        if coord[1] - 1 >= 0:
            if (coord[0], coord[1] - 1) in region and (coord[0], coord[1] - 1) not in checked:
                perimeter -= 2
        if coord[0] + 1 < len(grid):
            if (coord[0] + 1, coord[1]) in region and (coord[0] + 1, coord[1]) not in checked:
                perimeter -= 2
        if coord[1] + 1 < len(grid[0]):
            if (coord[0], coord[1] + 1) in region and (coord[0], coord[1] + 1) not in checked:
                perimeter -= 2
    price += perimeter * len(region)

print(price)
'''

# Part 2

grid = []

with open('2024/data/day12.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

regions = []
allPos = []

def makeRegion(y, x, coords):
    coords.add((y, x))
    if y - 1 >= 0:
        if grid[y][x] == grid[y - 1][x] and (y - 1, x) not in coords:
            coords.union(makeRegion(y - 1, x, coords))
    if x - 1 >= 0:
        if grid[y][x] == grid[y][x - 1] and (y, x - 1) not in coords:
            coords.union(makeRegion(y, x - 1, coords))
    if y + 1 < len(grid):
        if grid[y][x] == grid[y + 1][x] and (y + 1, x) not in coords:
            coords.union(makeRegion(y + 1, x, coords))
    if x + 1 < len(grid[0]):
        if grid[y][x] == grid[y][x + 1] and (y, x + 1) not in coords:
            coords.union(makeRegion(y, x + 1, coords))
    return coords

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in allPos:
            new = makeRegion(i, j, set())
            regions.append(sorted(list(new)))
            allPos.extend(list(new))

price = 0

for region in regions:
    perimeter = 0
    if len(region) == 1 or len(region) == 2:
        price += 4 * len(region)
        continue
    lastVert = (-1, -1)
    lastHor = (-1, -1)
    checked = set()
    for coord in region:
        checked.add(coord)
        if (coord[0] - 1, coord[1]) not in checked and ((coord[0], coord[1] - 1) not in checked or (coord[0] - 1, coord[1] - 1) in checked):
            perimeter += 1
        if (coord[0] + 1, coord[1]) not in region and ((coord[0], coord[1] - 1) not in checked or (coord[0] + 1, coord[1] - 1) in region):
            perimeter += 1
        if (coord[0], coord[1] - 1) not in checked and ((coord[0] - 1, coord[1]) not in checked or (coord[0] - 1, coord[1] - 1) in checked):
            perimeter += 1
        if (coord[0], coord[1] + 1) not in region and ((coord[0] - 1, coord[1]) not in checked or (coord[0] - 1, coord[1] + 1) in region):
            perimeter += 1
    price += perimeter * len(region)

print(price)