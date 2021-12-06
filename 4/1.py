from sys import stderr

with open("input", 'r') as file:
    input = list(map(lambda x : x.strip(), file.readlines()))

# RNs
nums = list(map(int,
	input.pop(0).split(',')
)) # pop(0) for next

boards = [
	[[], [], [], [], []]
]*(len(input)//6)

bc = -1# board count

while input:
	line = input.pop(0)
	if line:
		stderr.write("bruh: %s, %d\n" % (line, bc))
	else:
		boards[bc] = [
			input.pop(0),
			input.pop(0),
			input.pop(0),
			input.pop(0),
			input.pop(0),
		]
		print(boards[bc])
		bc+=1

# get n from nums
def rng() -> int:
	global nums
	if nums:
		return nums.pop(0)
	else:
		return -1

