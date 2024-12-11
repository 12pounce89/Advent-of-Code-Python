'''
# Part 1

possible = 0

with open('2016/data/day3.txt') as file:
    for line in file:
        sides = line.strip().split()
        sides[0], sides[1], sides[2] = int(sides[0]), int(sides[1]), int(sides[2])
        if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
            possible += 1

print(possible)
'''

# Part 2

possible = 0
triangles = []

with open('2016/data/day3.txt') as file:
    listed = list(file)
    for i in range(0, len(listed) - 2, 3):
        line1 = listed[i].strip().split()
        line2 = listed[i + 1].strip().split()
        line3 = listed[i + 2].strip().split()
        triangles.append([line1[0], line2[0], line3[0]])
        triangles.append([line1[1], line2[1], line3[1]])
        triangles.append([line1[2], line2[2], line3[2]])

for triangle in triangles:
    triangle[0], triangle[1], triangle[2] = int(triangle[0]), int(triangle[1]), int(triangle[2])
    if triangle[0] + triangle[1] > triangle[2] and triangle[0] + triangle[2] > triangle[1] and triangle[1] + triangle[2] > triangle[0]:
        possible += 1

print(possible)