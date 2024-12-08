'''
# Part 1

lines = []

with open('2023/data/day9.txt') as file:
    for line in file:
        lines.append(line.strip().split())

sum = 0

for line in lines:
    differences = [[]]
    iterations = 0
    different = True
    while different:
        if iterations == 0:
            for i in range(len(line) - 1):
                differences[iterations].append(int(line[i + 1]) - int(line[i]))
        else:
            for i in range(len(differences[iterations - 1]) - 1):
                differences[iterations].append(int(differences[iterations - 1][i + 1]) - int(differences[iterations - 1][i]))
        different = False
        iterations += 1
        differences.append([])
        for item in differences[iterations - 1]:
            if int(item) != 0:
                different = True
    for i in range(len(differences) - 3, -1, -1):
        differences[i].append(differences[i + 1][-1] + differences[i][-1])
    line.append(differences[0][-1] + int(line[-1]))
    sum += int(line[-1])

print(sum)
'''

# Part 2

lines = []

with open('2023/data/day9.txt') as file:
    for line in file:
        lines.append(line.strip().split())

sum = 0

for line in lines:
    differences = [[]]
    iterations = 0
    different = True
    while different:
        if iterations == 0:
            for i in range(len(line) - 1):
                differences[iterations].append(int(line[i + 1]) - int(line[i]))
        else:
            for i in range(len(differences[iterations - 1]) - 1):
                differences[iterations].append(int(differences[iterations - 1][i + 1]) - int(differences[iterations - 1][i]))
        different = False
        iterations += 1
        differences.append([])
        for item in differences[iterations - 1]:
            if int(item) != 0:
                different = True
    for i in range(len(differences) - 3, -1, -1):
        differences[i].insert(0, differences[i][0] - differences[i + 1][0])
    line.insert(0, int(line[0]) - differences[0][0])
    sum += int(line[0])

print(sum)