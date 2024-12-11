'''
# Part 1

x = 1
y = 1
password = ""

with open('2016/data/day2.txt') as file:
    for line in file:
        for char in line:
            if char == "U" and y > 0:
                y -= 1
            elif char == "D" and y < 2:
                y += 1
            elif char == "L" and x > 0:
                x -= 1
            elif char == "R" and x < 2:
                x += 1
        password += str(y * 3 + x + 1)

print(password)
'''

# Part 2

x = 0
y = 2
password = ""
up = [(2, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3), (2, 4)]
left = [(1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 2)]
down = [(2, 3), (2, 0), (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)]
right = [(3, 2), (0, 2), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
grid = [[" ", " ", "1", " ", " "], [" ", "2", "3", "4", " "], ["5", "6", "7", "8", "9"], [" ", "A", "B", "C", " "], [" ", " ", "D", " ", " "]]

with open('2016/data/day2.txt') as file:
    for line in file:
        for char in line.strip():
            if char == "U" and (x, y) in up:
                y -= 1
            elif char == "D" and (x, y) in down:
                y += 1
            elif char == "L" and (x, y) in left:
                x -= 1
            elif char == "R" and (x, y) in right:
                x += 1
        password += grid[y][x]

print(password)