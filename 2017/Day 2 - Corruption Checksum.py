'''
# Part 1

sum = 0

with open('2017/data/day2.txt') as file:
    for line in file:
        nums = line.strip().split()
        max = int(nums[0])
        min = int(nums[0])
        for num in nums:
            if int(num) > max:
                max = int(num)
            if int(num) < min:
                min = int(num)
        sum += max - min

print(sum)
'''

# Part 2

sum = 0

with open('2017/data/day2.txt') as file:
    for line in file:
        nums = line.strip().split()
        for i in range(len(nums)):
            num = nums.pop(i)
            for j in range(len(nums)):
                if float(int(int(num) / int(nums[j]))) == int(num) / int(nums[j]):
                    sum += int(num) / int(nums[j])
            nums.insert(i, num)

print(int(sum))