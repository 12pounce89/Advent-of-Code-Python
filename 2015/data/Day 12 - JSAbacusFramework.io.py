'''
# Part 1

sum = 0

with open('2015/data/day12.txt') as file:
    for line in file:
        line = line.strip()
        string = []
        for char in line:
            if char == "-":
                negative = True
            else:
                try:
                    num = int(char)
                    string.append(char)
                except:
                    if len(string) > 0:
                        if negative:
                            sum -= int("".join(string))
                        else:
                            sum += int("".join(string))
                    negative = False
                    string = []

print(sum)
'''

# Part 2

import json

def check(value):
    if type(value) == int:
        return value
    if type(value) == list:
        return sum([check(i) for i in value])
    if type(value) == dict:
        if "red" in value.values():
            return 0
        sums = []
        for key in value:
            sums.append(check(value[key]))
        return sum(sums)
    return 0

with open('2015/data/day12.txt') as file:
    for line in file:
        line = line.strip()
        loaded = json.loads(line)

print(check(loaded))