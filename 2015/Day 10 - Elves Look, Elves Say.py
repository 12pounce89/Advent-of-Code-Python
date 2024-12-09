'''
# Part 1

string = ""

with open('2015/data/day10.txt') as file:
    for line in file:
        string += line.strip()

for i in range(40):
    listed = [[string[0]]]
    for char in string[1:]:
        if char == listed[-1][0]:
            listed[-1] += char
        else:
            listed.append([char])
    string = ""
    for item in listed:
        string += str(len(item)) + item[0]

print(len(string))
'''

# Part 2

string = ""

with open('2015/data/day10.txt') as file:
    for line in file:
        string += line.strip()

for i in range(50):
    lastChar = string[0]
    count = 1
    result = []
    for char in string[1:]:
        if char == lastChar:
            count += 1
        else:
            result.append(str(count))
            result.append(lastChar)
            lastChar = char
            count = 1
    result.append(str(count))
    result.append(lastChar)
    string = "".join(result)

print(len(string))