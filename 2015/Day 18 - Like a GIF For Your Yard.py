'''
# Part 1

grid1 = []
grid2 = []
directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

with open('2015/data/day18.txt') as file:
    for line in file:
        grid1.append(list(line.strip()))
        grid2.append(["." for i in range(len(line.strip()))])

for trial in range(100):
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            surrounding = 0
            if trial % 2 == 0:
                grid2[i][j] = "."
                for item in directions:
                    y, x = i + item[0], j + item[1]
                    if (0 <= y < len(grid1) and 0 <= x < len(grid1[i])):
                        if grid1[y][x] == "#":
                            surrounding += 1
                        y -= item[0]
                        x -= item[1]
                if grid1[i][j] == "#" and 2 <= surrounding <= 3:
                    grid2[i][j] = "#"
                elif grid1[i][j] == "." and surrounding == 3:
                    grid2[i][j] = "#"
                else:
                    grid2[i][j] = "."
            else:
                for item in directions:
                    y, x = i + item[0], j + item[1]
                    if (0 <= y < len(grid1) and 0 <= x < len(grid1[i])):
                        if grid2[y][x] == "#":
                            surrounding += 1
                        y -= item[0]
                        x -= item[1]
                if grid2[i][j] == "#" and 2 <= surrounding <= 3:
                    grid1[i][j] = "#"
                elif grid2[i][j] == "." and surrounding == 3:
                    grid1[i][j] = "#"
                else:
                    grid1[i][j] = "."
    if grid1 == grid2:
        break

lights = 0

for line in grid1:
    for char in line:
        if char == "#":
            lights += 1

print(lights)
'''

# Part 2

grid1 = []
directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

with open('2015/data/day18.txt') as file:
    for line in file:
        grid1.append(list(line.strip()))

grid2 = [["." for i in range(len(grid1[j]))] for j in range(len(grid1))]
grid1[0][0], grid1[0][-1], grid1[-1][0], grid1[-1][-1] = "#", "#", "#", "#"
grid2[0][0], grid2[0][-1], grid2[-1][0], grid2[-1][-1] = "#", "#", "#", "#"

for trial in range(100):
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            surrounding = 0
            if trial % 2 == 0:
                grid2[i][j] = "."
                for item in directions:
                    y, x = i + item[0], j + item[1]
                    if (0 <= y < len(grid1) and 0 <= x < len(grid1[i])):
                        if grid1[y][x] == "#":
                            surrounding += 1
                if grid1[i][j] == "#" and 2 <= surrounding <= 3:
                    grid2[i][j] = "#"
                elif grid1[i][j] == "." and surrounding == 3:
                    grid2[i][j] = "#"
                else:
                    grid2[i][j] = "."
            else:
                for item in directions:
                    y, x = i + item[0], j + item[1]
                    if (0 <= y < len(grid1) and 0 <= x < len(grid1[i])):
                        if grid2[y][x] == "#":
                            surrounding += 1
                if grid2[i][j] == "#" and 2 <= surrounding <= 3:
                    grid1[i][j] = "#"
                elif grid2[i][j] == "." and surrounding == 3:
                    grid1[i][j] = "#"
                else:
                    grid1[i][j] = "."
    grid1[0][0], grid1[0][-1], grid1[-1][0], grid1[-1][-1] = "#", "#", "#", "#"
    grid2[0][0], grid2[0][-1], grid2[-1][0], grid2[-1][-1] = "#", "#", "#", "#"

lights = 0

for line in grid1:
    for char in line:
        if char == "#":
            lights += 1

print(lights)