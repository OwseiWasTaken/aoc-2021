#! /bin/python3.10
inputs:list[str] = []
with open("1.i", 'r') as f:
	inputs = f.readlines()

now = 0
prev = 0
big = 0
inlen = len(inputs)
for i in range(len(inputs)):
	if i+3 > inlen:break
	now = int(inputs[i])
	now += int(inputs[i+1])
	now += int(inputs[i+2])
	if now > prev and prev:
		big+=1
	prev = now
print(big)
