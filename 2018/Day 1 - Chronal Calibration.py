'''
# Part 1

nums = []

with open('2018/data/day1.txt') as file:
    for line in file:
        nums.append(int(line.strip()))

print(sum(nums))
'''

# Part 2

nums = []

with open('2018/data/day1.txt') as file:
    for line in file:
        nums.append(int(line.strip()))

index = 0
frequency = 0
freqs = set()

while True:
    frequency += nums[index]
    if frequency in freqs:
        break
    index = (index + 1) % len(nums)
    freqs.add(frequency)

print(frequency)