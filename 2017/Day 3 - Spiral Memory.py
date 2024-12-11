# Part 1

target = ""

with open('2017/data/day3.txt') as file:
    for line in file:
        target += line.strip()
target = int(target)
test = 1

while (test + 2) ** 2 < target:
    test += 2

side = int((((test + 2) ** 2) - (test ** 2)) / 4)
diff = target - test ** 2
distance = 2 * (test // 2)
i = 0

while i < diff:
    if i == 0:
        distance += 1
    elif 0 <= i % side < side // 2:
        distance -= 1
    else:
        distance += 1
    i += 1

print(distance)