#! /bin/python3.10
inputs:list[str] = []
with open("i", 'r') as f:
	inputs = f.readlines()

old = 0
bigger = 0
for i in inputs:
	i = int(i[:-1]) # [:-1] cut \n
	if i > old and old:
		bigger += 1
	old = i
print(bigger)
