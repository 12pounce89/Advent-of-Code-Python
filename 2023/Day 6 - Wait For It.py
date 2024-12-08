# Part 1
'''
values = []

with open('2023/data/day6.txt') as file:
    for line in file:
        broken_line = line.split(":")
        values.append(broken_line[1].strip().split())

values.append([])

for i in range(len(values[0])):
    values[2].append(0)
    for j in range(1, int(values[0][i]) // 2 + 1):
        if ((j * (int(values[0][i]) - j)) > int(values[1][i])):
            values[2][i] += 1
    values[2][i] *= 2
    if ((int(values[0][i]) % 2 == 0)):
        values[2][i] -= 1

product = 1
for item in values[2]:
    product *= item

print(product)
'''

# Part 2

values = []

with open('2023/data/day6.txt') as file:
    for line in file:
        broken_line = line.split(":")
        values.append(broken_line[1].strip().split())

time = ""
for item in values[0]:
    time += item
time = int(time)

distance = ""
for item in values[1]:
    distance += item
distance = int(distance)

options = 0

for i in range(1, time // 2 + 1):
    if ((i * (time - i)) > distance):
        options += 1
options *= 2
if ((time % 2 == 0)):
    options -= 1

print(options)