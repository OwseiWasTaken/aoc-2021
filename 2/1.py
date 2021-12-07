#! /bin/python3.10
inputs:list[str] = []
with open("i", 'r') as f:
	inputs = f.readlines()
x = 0
y = 0

for line in inputs:
	line = line.replace(
		"forward ","f"
	).replace(
		"down ","d"
	).replace(
		"up ","u"
	)
	cont = int(line[1:])
	if line[0] == 'f':
		x+=cont
	elif line[0] == 'u':
		y-=cont
	else:
		y+=cont
print(x, y)
print(x*y)

