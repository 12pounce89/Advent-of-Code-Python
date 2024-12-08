# Part 1
'''
bag = {'red':12, 'green':13, 'blue':14}
sum = 0
with open('2023/data/day2.txt') as file:
    for line in file:
        failed = False
        broken_line = line.split(":")
        draws = broken_line[1].split(";")
        for item in draws:
            colors = item.split(',')
            for item in colors:
                amounts = item.strip().split()
                if (int(amounts[0]) > bag.get(amounts[1])):
                    failed = True
                    break
            if failed:
                break
        if not failed:
            game = broken_line[0].split()
            sum += int(game[1])

print(sum)
'''

# Part 2

sum = 0
with open('2023/data/day2.txt') as file:
    for line in file:
        bag = {'red':0, 'green':0, 'blue':0}
        broken_line = line.split(":")
        draws = broken_line[1].split(";")
        for item in draws:
            colors = item.split(',')
            for item in colors:
                amounts = item.strip().split()
                if (int(amounts[0]) > bag.get(amounts[1])):
                    bag[amounts[1]] = int(amounts[0])
        sum += bag.get('red') * bag.get('green') * bag.get('blue')

print(sum)