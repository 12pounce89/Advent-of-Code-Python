'''
# Part 1

grid = []
grid2 = []
moves = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}

with open('2024/data/day16.txt') as file:
    for line in file:
        grid.append(list(line.strip()))
        grid2.append(list(line.strip()))

found1, found2 = False, False

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
            found1 = True
            break
        elif char == "E":
            end = (i, j)
            found2 = True
            break
    if found1 and found2:
        break

positions = [(0, start[0], start[1], 1)]
visited = set()

while len(positions) > 0:
    minCost = positions[0][0]
    minIndex = 0
    for i in range(1, len(positions)):
        if positions[i][0] < minCost:
            minIndex = i
            minCost = positions[i][0]
    
    cost, y, x, direction = positions.pop(minIndex)

    if (y, x) == end:
        print(cost)
        break

    if (y, x, direction) in visited:
        continue
    visited.add((y, x, direction))

    dy, dx = moves[direction]
    newY = y + dy
    newX = x + dx
    if grid[newY][newX] != "#":
        positions.append((cost + 1, newY, newX, direction))
    
    positions.append((cost + 1000, y, x, (direction + 1) % 4))
    positions.append((cost + 1000, y, x, (direction - 1) % 4))
'''
# Working recursive solution for part 1 examples, but doesn't work for the full input since it's too long
'''
def move(pos, visited=set(), facing=1, points=0):
    visited.add(pos)
    if len(finishedPoints) > 0:
        if points > min(finishedPoints):
            return
    # print(visited)
    y, x = pos
    a, b = moves[facing]
    c, d = moves[(facing + 1) % 4]
    e, f = moves[(facing - 1) % 4]

    if (y + a, x + b) in visited:
        pass
    elif grid[y + a][x + b] == "E":
        finishedPoints.add(points + 1)
    elif grid[y + a][x + b] == ".":
        move((y + a, x + b), visited, facing, points + 1)
        visited.remove((y + a, x + b))

    if (y + c, x + d) in visited:
        pass
    elif grid[y + c][x + d] == "E":
        finishedPoints.add(points + 1001)
    elif grid[y + c][x + d] == ".":
        move((y + c, x + d), visited, (facing + 1) % 4, points + 1001)
        visited.remove((y + c, x + d))

    if (y + e, x + f) in visited:
        pass
    elif grid[y + e][x + f] == "E":
        finishedPoints.add(points + 1001)
    elif grid[y + e][x + f] == ".":
        move((y + e, x + f), visited, (facing - 1) % 4, points + 1001)
        visited.remove((y + e, x + f))
'''

# Part 2

grid = []
grid2 = []
moves = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}

with open('2024/data/tester.txt') as file:
    for line in file:
        grid.append(list(line.strip()))
        grid2.append(list(line.strip()))

found1, found2 = False, False

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
            found1 = True
            break
        elif char == "E":
            end = (i, j)
            found2 = True
            break
    if found1 and found2:
        break

positions = [(0, start[0], start[1], 1, ((start[0], start[1], 1),))]
visited = set()
onBest = set()
bestCost = -1
p = 0

while len(positions) > 0:
    p += 1
    minCost = positions[0][0]
    minIndex = 0
    for i in range(1, len(positions)):
        if positions[i][0] < minCost:
            minIndex = i
            minCost = positions[i][0]
    
    cost, y, x, direction, path = positions.pop(minIndex)

    # if (9, 3, 1) in path and (7, 4, 1) in path:
    #     print(cost, y, x, direction, path)

    if (y, x) == end:
        print('test', bestCost, cost)
        if bestCost == -1:
            bestCost = cost
        if cost == bestCost:
            print(path)
            for item in path:
                onBest.add(item)
        continue

    if bestCost != -1 and cost >= bestCost:
        for item in path:
            if item in visited:
                visited.remove(item)
        continue

    if (y, x, direction) in visited:
        for item in path:
            if item in visited:
                visited.remove(item)
        # if (y, x, direction) not in onBest:
        #     continue
    else:
        visited.add((y, x, direction))

    dy, dx = moves[direction]
    newY = y + dy
    newX = x + dx
    if grid[newY][newX] != "#":
        # if len(path) == 0:
        #     path = (start, (newY, newX))
        #     print(path)
        # else:
        newPath1 = path + ((newY, newX, direction),)
        positions.append((cost + 1, newY, newX, direction, newPath1))
    
    newPath2 = path + ((y, x, (direction + 1) % 4),)
    positions.append((cost + 1000, y, x, (direction + 1) % 4, newPath2))
    newPath3 = path + ((y, x, (direction - 1) % 4),)
    positions.append((cost + 1000, y, x, (direction - 1) % 4, newPath3))

print(sorted(list(onBest)))
print(p)

bestCoords = set()
for item in onBest:
    bestCoords.add((item[0], item[1]))
print(len(bestCoords))

for pos in bestCoords:
    grid2[pos[0]][pos[1]] = "O"

for line in grid2:
    print("".join(line))