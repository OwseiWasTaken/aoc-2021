with open("input", 'r') as file:
    input = file.readlines()

nums = list(map(int, input[0][:-1].split(','))) # pop(0) for next
print(nums)