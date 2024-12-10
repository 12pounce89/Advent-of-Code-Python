'''
# Part 1

def check_route(y, x, ends, num = 0):
    if grid[y][x] == '9':
        if (y, x) not in ends:
            ends.append((y, x))
        return 
    if y > 0:
        if grid[y - 1][x] == str(num + 1):
            check_route(y - 1, x, ends, num + 1)
    if x > 0:
        if grid[y][x - 1] == str(num + 1):
            check_route(y, x - 1, ends, num + 1)
    if y < len(grid) - 1:
        if grid[y + 1][x] == str(num + 1):
            check_route(y + 1, x, ends, num + 1)
    if x < len(grid[y]) - 1:
        if grid[y][x + 1] == str(num + 1):
            check_route(y, x + 1, ends, num + 1)
    return len(ends)

grid = []

with open('2024/data/day10.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

found = 0
previous = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '0':
            previous = found
            found += check_route(i, j, [])

print(found)
'''

# Part 2

def check_route(y, x, num = 0):
    score = 0
    if grid[y][x] == '9':
        return 1
    if y > 0:
        if grid[y - 1][x] == str(num + 1):
            score += check_route(y - 1, x, num + 1)
    if x > 0:
        if grid[y][x - 1] == str(num + 1):
            score += check_route(y, x - 1, num + 1)
    if y < len(grid) - 1:
        if grid[y + 1][x] == str(num + 1):
            score += check_route(y + 1, x, num + 1)
    if x < len(grid[y]) - 1:
        if grid[y][x + 1] == str(num + 1):
            score += check_route(y, x + 1, num + 1)
    return score

grid = []

with open('2024/data/day10.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

found = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '0':
            found += check_route(i, j)

print(found)