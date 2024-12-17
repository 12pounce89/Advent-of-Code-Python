# Part 1

regA = 0
regB = 0
regC = 0
commands = []

with open('2024/data/tester.txt') as file:
    for line in file:
        if line.strip() != "":
            broken = line.strip().split(": ")
            if broken[0] == "Program":
                input = broken[1].split(",")
                commands += input
            else:
                moreBroken = broken[0].split()
                if moreBroken[0] == "Register":
                    if moreBroken[1] == "A":
                        regA = int(broken[1])
                    elif moreBroken[1] == "B":
                        regB = int(broken[1])
                    elif moreBroken[1] == "C":
                        regC = int(broken[1])

for i in range(0, len(commands), 2):
    