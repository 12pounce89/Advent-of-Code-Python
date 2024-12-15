'''
# Part 1

grid = []
directions = ""
makingGrid = True

with open('2024/data/day15.txt') as file:
    for line in file:
        if line.strip() == "":
            makingGrid = False
        if makingGrid:
            grid.append(list(line.strip()))
        else:
            directions += line.strip()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)


directions = list(directions)
moves = {'^':(-1, 0), '>':(0, 1), '<':(0, -1), 'v':(1, 0)}

for direction in directions:
    vert, hor = moves[direction]
    y, x = robot[0] + vert, robot[1] + hor
    running = True
    while running:
        if grid[y][x] == 'O':
            y, x = y + vert, x + hor
        elif grid[y][x] == '#':
            running = False
            break
        elif grid[y][x] == ".":
            running = False
            if y == robot[0] + vert and x == robot[1] + hor:
                grid[y][x] = "@"
                grid[robot[0]][robot[1]] = "."
                robot = (y, x)
            else:
                grid[y][x] = "O"
                grid[robot[0]][robot[1]] = "."
                grid[robot[0] + vert][robot[1] + hor] = "@"
                robot = (robot[0] + vert, robot[1] + hor)
            break

gps = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "O":
            gps += 100 * (i) + j

print(gps)
'''

# Part 2

oldGrid = []
directions = ""
makingGrid = True

with open('2024/data/day15.txt') as file:
    for line in file:
        if line.strip() == "":
            makingGrid = False
        if makingGrid:
            oldGrid.append(list(line.strip()))
        else:
            directions += line.strip()

grid = []

for line in oldGrid:
    row = []
    for char in line:
        if char == "@":
            row.extend(["@", "."])
        elif char == "O":
            row.extend(["[", "]"])
        else:
            row.extend([char, char])
    grid.append(row)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)

directions = list(directions)
moves = {'^':(-1, 0), '>':(0, 1), '<':(0, -1), 'v':(1, 0)}

for direction in directions:
    vert, hor = moves[direction]
    y, x = robot[0] + vert, robot[1] + hor
    running = True
    if vert == 0:
        coords = [[robot, "@"]]
        while running:
            if grid[y][x] == '[' or grid[y][x] == ']':
                coords.append([(y, x), grid[y][x]])
                y, x = y + vert, x + hor
            elif grid[y][x] == '#':
                running = False
                break
            elif grid[y][x] == ".":
                running = False
                if y == robot[0] + vert and x == robot[1] + hor:
                    grid[y][x] = "@"
                    grid[robot[0]][robot[1]] = "."
                    robot = (y, x)
                else:
                    for i in range(len(coords) - 1, -1, -1):
                        a, b = coords[i][0]
                        grid[a + vert][b + hor] = coords[i][1]
                        grid[a][b] = "."
                    robot = (robot[0] + vert, robot[1] + hor)
                break
    else:
        coords = [[robot, "@"]]
        top = {robot}
        while running:
            empty = True
            newTop = set()
            for a, b in top:
                c, d = a + vert, b + hor
                if grid[c][d] == "#":
                    running = False
                    empty = False
                    break
                elif grid[c][d] == "[":
                    coords.append([(c, d), "["])
                    coords.append([(c, d + 1), "]"])
                    newTop.add((c, d))
                    newTop.add((c, d + 1))
                    empty = False
                elif grid[c][d] == "]":
                    coords.append([(c, d), "]"])
                    coords.append([(c, d - 1), "["])
                    newTop.add((c, d))
                    newTop.add((c, d - 1))
                    empty = False
                y, x = y + vert, x + hor
            top = newTop
            if empty:
                for i in range(len(coords) - 1, -1, -1):
                    a, b = coords[i][0]
                    grid[a + vert][b + hor] = coords[i][1]
                    grid[a][b] = "."
                robot = (robot[0] + vert, robot[1] + hor)
                break

gps = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "[":
            gps += 100 * (i) + j

print(gps)