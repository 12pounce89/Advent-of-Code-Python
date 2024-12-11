'''
# Part 1

stones = []

with open('2024/data/day11.txt') as file:
    for line in file:
        stones += line.strip().split()

stones = [int(x) for x in stones]

for _ in range(25):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            stones.insert(i + 1, int(str(stones[i])[int(len(str(stones[i])) / 2):]))
            stones[i] = int(str(stones[i])[:int(len(str(stones[i])) / 2)])
            i += 1
        else:
            stones[i] *= 2024
        i += 1

print(len(stones))
'''

# Part 2

stones = []

with open('2024/data/day11.txt') as file:
    for line in file:
        stones += line.strip().split()

stones = [int(x) for x in stones]
rules = {0:[1]}
current_stones = {}

for stone in stones:
    if stone not in current_stones:
        current_stones[stone] = 0
    current_stones[stone] += 1

for run in range(75):
    new_stones = {}
    for stone in current_stones:
        if stone in rules:
            pass
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            a = int(str_stone[:mid])
            b = int(str_stone[mid:])
            rules[stone] = [a, b]
        else:
            rules[stone] = [stone * 2024]
        for item in rules[stone]:
            if item not in new_stones:
                new_stones[item] = 0
            new_stones[item] += 1 * current_stones[stone]
    current_stones = new_stones
    sum = 0
    for key in current_stones:
        sum += current_stones[key]

sum = 0

for key in current_stones:
    sum += current_stones[key]

print(sum)