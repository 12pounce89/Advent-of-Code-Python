# Part 1

grid1 = []
grid2 = []
directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

with open('2015/data/tester.txt') as file:
    for line in file:
        grid1.append(list(line.strip()))
        grid2.append(["." for i in range(len(line.strip()))])

for line in grid1:
    print("".join(line))
print()


for trial in range(6):
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            surrounding = 0
            if trial % 2 == 0:
                grid2[i][j] = "."
                for item in directions:
                    y, x = i, j
                    try:
                        y += item[0]
                        x += item[1]
                        if grid1[y][x] == "#":
                            surrounding += 1
                        y -= item[0]
                        x -= item[1]
                    except:
                        pass
                    if grid1[i][j] == "#" and 2 <= surrounding <= 3:
                        grid2[i][j] = "#"
                    elif grid1[i][j] == "." and surrounding == 3:
                        grid2[i][j] = "#"
                    else:
                        grid2[i][j] = "."
            else:
                for item in directions:
                    y, x = i, j
                    try:
                        y += item[0]
                        x += item[1]
                        if grid2[y][x] == "#":
                            surrounding += 1
                        y -= item[0]
                        x -= item[1]
                    except:
                        pass
                    if grid2[i][j] == "#" and 2 <= surrounding <= 3:
                        grid1[i][j] = "#"
                    elif grid2[i][j] == "." and surrounding == 3:
                        grid1[i][j] = "#"
                    else:
                        grid1[i][j] = "."
    if trial % 2 == 0:
        for line in grid2:
            print("".join(line))
        print()
    else:
        for line in grid1:
            print("".join(line))
        print()
    if grid1 == grid2:
        break

lights = 0

for line in grid1:
    for char in line:
        if char == "#":
            lights += 1

print(lights)