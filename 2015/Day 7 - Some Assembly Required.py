# Part 1

def myBin(x):
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % 2) + result
        x //= 2
    return result

commands = dict()
wires = dict()

with open('2015/data/day7.txt') as file:
    for line in file:
        operation, result = line.strip().split(" -> ")
        commands[result.strip()] = operation.strip().split()

def calculate(value):
    try:
        return int(value)
    except:
        pass

    if value not in wires:
        operators = commands[value]
        if len(operators) == 1:
            result = calculate(operators[0])
        else:
            operator = operators[-2]
            if operator == "AND":
                result = calculate(operators[0]) & calculate(operators[2])
            elif operator == 'OR':
                result = calculate(operators[0]) | calculate(operators[2])
            elif operator == 'NOT':
                result = ~calculate(operators[1]) & 0xffff
            elif operator == 'RSHIFT':
                result = calculate(operators[0]) >> calculate(operators[2])
            elif operator == 'LSHIFT':
                result = calculate(operators[0]) << calculate(operators[2])
        wires[value] = result
    return wires[value]

print(calculate("a"))












'''
for line in commands:
    if line[-1] not in wires:
        wires[line[-1]] = ""
    try:
        wires[line[-1]] = myBin(int(line[0]))[2:]
    except:
        broken = line[0].split()
        if broken[0] == "NOT":
            binary = ""
            for i in range(len(wires[broken[1]]) - 1, -1, -1):
                binary += str((int(list(wires[broken[1]])[i]) + 1) % 2)
            for i in range(16 - len(binary)):
                binary = "0" + binary
            wires[line[-1]] = binary
        elif broken[1] == "AND":
            binary = ""
            for i in range(16):
                if broken[0][i] == "1" and broken[2][i] == "1":
                    binary += "1"
                else:
                    binary += "0"
            wires[line[-1]] = binary
        elif broken[1] == "OR":
            binary = ""
            for i in range(16):
                if broken[0][i] == "1" or broken[2][i] == "1":
                    binary += "1"
                else:
                    binary += "0"
            wires[line[-1]] = binary
        elif broken[1] == "LSHIFT":
            binary = wires[broken[0]][int(broken[2]) - 1:]
            for i in range(int(broken[2])):
                binary += "0"
            wires[line[-1]] = binary
        elif broken[1] == "RSHIFT":
            binary = wires[broken[0]][:16 - int(broken)]
            for i in range(int(broken[2])):
                binary = "0" + binary
            wires[line[-1]] = binary

print(int(wires["a"], 2))
'''