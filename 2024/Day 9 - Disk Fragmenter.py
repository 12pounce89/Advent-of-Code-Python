# Part 1

map = ""

with open('2024/data/day9.txt') as file:
    for line in file:
        map += line.strip()

id = 0
grid = []
grid2 = []

for i, char in enumerate(map):
    if i % 2 == 0:
        for i in range(int(char)):
            grid.append(str(id))
            grid2.append(str(id))
        id += 1
    else:
        for i in range(int(char)):
            grid.append(".")
            grid2.append(".")

reversePos = len(grid) - 1
# print("".join(grid))
for i, char in enumerate(grid):
    if char == ".":
        while grid[reversePos] == ".":
            reversePos -= 1
            # print("test")
        if reversePos >= i:
            grid2[i] = grid[reversePos]
            grid2[reversePos] = "."
            reversePos -= 1

checkSum = 0

for i, char in enumerate(grid2):
    if char == ".":
        break
    checkSum += i * int(char)

print(checkSum)