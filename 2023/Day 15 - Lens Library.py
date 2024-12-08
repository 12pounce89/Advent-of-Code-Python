'''
# Part 1

import csv

with open('data/day15.txt') as file:
    csvReader = csv.reader(file)
    sum = 0

    for line in csvReader:
        for item in line:
            hashed = 0
            for char in item:
                hashed = ((hashed + ord(char)) * 17) % 256
            sum += hashed

print(sum)
'''

# Part 2

import csv

boxes = dict()
for i in range(256):
    boxes[i] = []

with open('data/day15.txt') as file:
    csvReader = csv.reader(file)

    for line in csvReader:
        for item in line:
            hashed = 0
            for char in item:
                hashed = ((hashed + ord(char)) * 17) % 256
            if "=" in item:
                split = item.split("=")
                boxes[hashed].append(split)
            elif "-" in item:
                split = item.split("-")
                for pos, value in enumerate(boxes[hashed]):
                    if split[0] == value[0]:
                        boxes[hashed].pop(pos)

    power = 0
    for key in boxes:
        for i in range(len(boxes[key])):
            power += (key + 1) * (i + 1) * int(boxes[key][i][1])

print(power)