# Part 1
'''
points = 0
with open('2023/data/day4.txt') as file:
    for line in file:
        broken_line = line.split(':')
        more_broken_line = broken_line[1].split("|")
        winners = more_broken_line[0].strip().split()
        mine = more_broken_line[1].strip().split()
        count = 0
        for item in mine:
            if item in winners:
                count += 1
        if (count > 0):
            points += 2**(count - 1)

print(points)
'''

# Part 2

tester = 0
cards = dict()
with open('2023/data/day4.txt') as file:
    for line in file:
        broken_line = line.split(':')
        number = int(broken_line[0].split()[1].strip())
        cards[number] = 1
with open('data/day4.txt') as file:
    for line in file:
        broken_line = line.split(':')
        number = int(broken_line[0].split()[1].strip())
        more_broken_line = broken_line[1].split("|")
        winners = more_broken_line[0].strip().split()
        mine = more_broken_line[1].strip().split()
        count = 0
        for item in mine:
            if item in winners:
                count += 1
        if (count > 0):
            for i in range(count):
                if ((number + 1 + i) in cards):
                    cards[number + 1 + i] += cards.get(number)

card_total = 0
for key in cards:
    card_total += cards[key]
print(card_total)