# Part 1
'''
import re
sum = 0
with open('data/day1.txt') as file:
    for line in file:
        sum += int(str(re.findall('[1-9]', line)[0]) + str(re.findall('[1-9]', line)[-1]))
print(sum)
'''

# Part 2

import re
sum = 0
numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
with open('data/day1.txt') as file:
    for line in file:
        nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))', line)

        try:
            num1 = int(nums[0])
        except:
            num1 = numbers.get(nums[0])
        try:
            num2 = int(nums[-1])
        except:
            num2 = numbers.get(nums[-1])
        sum += int(str(num1) + str(num2))
print(sum)