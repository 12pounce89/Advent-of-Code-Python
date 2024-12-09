'''
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
for i, char in enumerate(grid):
    if char == ".":
        while grid[reversePos] == ".":
            reversePos -= 1
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
'''

# Part 2

map = ""

with open('2024/data/day9.txt') as file:
    for line in file:
        map += line.strip()

id = 0
ids = []
spaces = []
grid1 = []
nums = []
grid2 = []

for i, char in enumerate(map):
    if i % 2 == 0:
        grid1.append([str(id) for i in range(int(char))])
        grid2.append([str(id) for i in range(int(char))])
        id += 1
    else:
        grid1.append(["." for i in range(int(char))])
        grid2.append(["." for i in range(int(char))])
    nums.append(int(char))

for i in range(len(nums) - 1, -1, -2):
    # for item in grid2:
    #     print("".join(item), end="")
    # print()
    pos = 1
    while pos < i:
        if nums[pos] >= nums[i]:
            broken = []
            if grid1[pos] != grid2[pos]:
                for j in range(nums[pos]):
                    grid2[pos][len(grid2[pos]) - (1 + j)] = grid2[i][0]
            else:
                grid2[pos] = grid2[i] + grid2[pos][nums[i]:]
            grid2[i] = ["." for _ in range(nums[i])]
            # print(grid1[pos], grid2[pos])
            nums[pos] -= nums[i]
            # print(nums[pos])
            break
        pos += 2

checkSum = 0

grid = []
for line in grid2:
    for char in line:
        grid.append(char)

for i, char in enumerate(grid):
    if char == ".":
        continue
    checkSum += i * int(char)

print(checkSum)