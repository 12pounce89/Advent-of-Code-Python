'''
# Part 1

import re

commands = []

with open('2015/data/day23.txt') as file:
    for line in file:
        commands.append(re.split(' |, ', line.strip()))

registers = {'a':0, 'b':0}
pos = 0

while 0 <= pos < len(commands):
    command = commands[pos]
    if command[0] == "jio":
        if registers[command[1]] == 1:
            if command[2][1] == "0":
                print("stuck in loop")
                break
            elif command[2][0] == '+':
                pos += int(command[2][1:])
            elif command[2][0] == "-":
                pos -= int(command[2][1:])
        else:
            pos += 1
        continue
    elif command[0] == "jie":
        if registers[command[1]] % 2 == 0:
            if command[2][1] == "0":
                print("stuck in loop")
                break
            elif command[2][0] == '+':
                pos += int(command[2][1:])
            elif command[2][0] == "-":
                pos -= int(command[2][1:])
        else:
            pos += 1
        continue
    elif command[0] == "jmp":
        if command[1][1] == "0":
            print("stuck in loop")
            break
        elif command[1][0] == "+":
            pos += int(command[1][1:])
        elif command[1][0] == "-":
            pos -= int(command[1][1:])
        continue
    elif command[0] == "hlf":
        registers[command[1]] /= 2
    elif command[0] == "tpl":
        registers[command[1]] *= 3
    elif command[0] == "inc":
        registers[command[1]] += 1
    pos += 1

print(registers['b'])
'''

# Part 2

import re

commands = []

with open('2015/data/day23.txt') as file:
    for line in file:
        commands.append(re.split(' |, ', line.strip()))

registers = {'a':1, 'b':0}
pos = 0

while 0 <= pos < len(commands):
    command = commands[pos]
    if command[0] == "jio":
        if registers[command[1]] == 1:
            if command[2][1] == "0":
                print("stuck in loop")
                break
            elif command[2][0] == '+':
                pos += int(command[2][1:])
            elif command[2][0] == "-":
                pos -= int(command[2][1:])
        else:
            pos += 1
        continue
    elif command[0] == "jie":
        if registers[command[1]] % 2 == 0:
            if command[2][1] == "0":
                print("stuck in loop")
                break
            elif command[2][0] == '+':
                pos += int(command[2][1:])
            elif command[2][0] == "-":
                pos -= int(command[2][1:])
        else:
            pos += 1
        continue
    elif command[0] == "jmp":
        if command[1][1] == "0":
            print("stuck in loop")
            break
        elif command[1][0] == "+":
            pos += int(command[1][1:])
        elif command[1][0] == "-":
            pos -= int(command[1][1:])
        continue
    elif command[0] == "hlf":
        registers[command[1]] /= 2
    elif command[0] == "tpl":
        registers[command[1]] *= 3
    elif command[0] == "inc":
        registers[command[1]] += 1
    pos += 1

print(registers['b'])