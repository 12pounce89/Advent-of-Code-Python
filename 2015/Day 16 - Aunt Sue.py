'''
# Part 1

import re

known = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}
possible = dict()

with open('2015/data/day16.txt') as file:
    for line in file:
        line = line.strip()
        broken = re.split(': |, ', line)
        if known[broken[1]] == int(broken[2]) and known[broken[3]] == int(broken[4]) and known[broken[5]] == int(broken [6]):
            possible[broken[0]] = broken

for key in possible:
    print(key, possible[key])
'''

# Part 2

import re

def gte(a, b):
    if a < b:
        return True
    return False

def lte(a, b):
    if a > b:
        return True
    return False

def eq(a, b):
    if a == b:
        return True
    return False

known = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}
greater = ['cats', 'trees']
lesser = ['pomeranians', 'goldfish']
possible = dict()

with open('2015/data/day16.txt') as file:
    for line in file:
        line = line.strip()
        broken = re.split(': |, ', line)
        operators = []
        if broken[1] in greater:
            operators.append(gte)
        elif broken[1] in lesser:
            operators.append(lte)
        else:
            operators.append(eq)
        if broken[3] in greater:
            operators.append(gte)
        elif broken[3] in lesser:
            operators.append(lte)
        else:
            operators.append(eq)
        if broken[5] in greater:
            operators.append(gte)
        elif broken[5] in lesser:
            operators.append(lte)
        else:
            operators.append(eq)
        if operators[0](known[broken[1]], int(broken[2])) and operators[1](known[broken[3]], int(broken[4])) and operators[2](known[broken[5]], int(broken [6])):
            possible[broken[0]] = broken

for key in possible:
    print(key, possible[key])