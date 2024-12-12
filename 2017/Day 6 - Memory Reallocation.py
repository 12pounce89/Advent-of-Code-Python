'''
# Part 1

grid = []

with open('2017/data/day6.txt') as file:
    for line in file:
        grid.extend(line.strip().split())

grid = [int(x) for x in grid]
checked = set()
steps = 0

while tuple(grid) not in checked:
    checked.add(tuple(grid))
    max = 0
    for i in range(1, len(grid)):
        if grid[i] > grid[max]:
            max = i
    value = grid[max]
    grid[max] = 0
    while value > 0:
        max = (max + 1) % len(grid)
        grid[max] += 1
        value -= 1
    steps += 1

print(steps)
'''

# Part 1

grid = []

with open('2017/data/day6.txt') as file:
    for line in file:
        grid.extend(line.strip().split())

grid = [int(x) for x in grid]
checked = {}
steps = 0

while tuple(grid) not in checked:
    checked[tuple(grid)] = steps
    max = 0
    for i in range(1, len(grid)):
        if grid[i] > grid[max]:
            max = i
    value = grid[max]
    grid[max] = 0
    while value > 0:
        max = (max + 1) % len(grid)
        grid[max] += 1
        value -= 1
    steps += 1

print(steps - checked[tuple(grid)])