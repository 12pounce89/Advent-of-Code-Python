'''
# Part 1

positions = []
grid = [["." for _ in range(71)] for _ in range(71)]

with open('2024/data/day18.txt') as file:
    for line in file:
        broken = line.strip().split(",")
        positions.append((int(broken[0]), int(broken[1])))

for i in range(1024):
    y, x = positions[i]
    grid[y][x] = "#"

checks = [(0, 0, 0)]
visited = set()

while len(checks) > 0:
    minCost = checks[0][0]
    minIndex = 0
    for i in range(1, len(checks)):
        if checks[i][0] < minCost:
            minIndex = i
            minCost = positions[i][0]
    
    cost, y, x = checks.pop(minIndex)

    if (y, x) == (70, 70):
        print(cost)
        break

    if (y, x) in visited:
        continue
    visited.add((y, x))

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dy, dx in directions:
        newY, newX = y + dy, x + dx
        if 0 <= newY <= 70 and 0 <= newX <= 70 and grid[newY][newX] != "#":
            checks.append((cost + 1, newY, newX))
'''

# Part 2

positions = []
grid = [["." for _ in range(71)] for _ in range(71)]

with open('2024/data/day18.txt') as file:
    for line in file:
        broken = line.strip().split(",")
        positions.append((int(broken[0]), int(broken[1])))

for i in range(1024):
    a, b = positions[i]
    grid[a][b] = "#"

for i in range(1024, len(positions)):
    a, b = positions[i]
    grid[a][b] = "#"

    checks = [(0, 0, 0)]
    visited = set()

    while len(checks) > 0:
        minCost = checks[0][0]
        minIndex = 0
        for i in range(1, len(checks)):
            if checks[i][0] < minCost:
                minIndex = i
                minCost = positions[i][0]
        
        cost, y, x = checks.pop(minIndex)

        if (y, x) == (70, 70):
            # print(cost)
            break

        if (y, x) in visited:
            continue
        visited.add((y, x))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dy, dx in directions:
            newY, newX = y + dy, x + dx
            if 0 <= newY <= 70 and 0 <= newX <= 70 and grid[newY][newX] != "#":
                checks.append((cost + 1, newY, newX))
    
    if len(checks) == 0:
        print(f"{str(a)}, {str(b)}")
        break