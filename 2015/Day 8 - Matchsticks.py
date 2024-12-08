'''
# Part 1

strings = []

with open('2015/data/day8.txt') as file:
    for line in file:
        strings.append(list(line.strip()))

total = 0
shrunk = 0

for line in strings:
    total += len(line)
    line.pop(-1)
    line.pop(0)
    index = 0
    while index < len(line):
        if line[index] == "\\":
            if line[index + 1] == "x":
                line = line[:index] + line[index + 4:]
            else:
                line = line[:index] + line[index + 2:]
            line.insert(index, "#")
        index += 1
    shrunk += len(line)

print(total - shrunk)
'''

# Part 2

strings1 = []
strings2 = []

with open('2015/data/day8.txt') as file:
    for line in file:
        strings1.append(list(line.strip()))
        strings2.append(list(line.strip()))

total = 0
new = 0

for i in range(len(strings1)):
    line1, line2 = strings1[i], strings2[i]
    total += len(line1)
    for j in range(len(line1)):
        if line1[j] == "\"" or line1[j] == "\\":
            line2.insert(-(j + 1), "\\")
    line2.insert(0, "\"")
    line2.append("\"")
    new += len(line2)

print(new - total)