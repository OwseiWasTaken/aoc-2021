#! /bin/python3.10
inputs:list[str] = []
with open("2.i", 'r') as f:
	inputs = f.readlines()

x = 0
y = 0
aim = 0

for line in inputs:
	oline = line #original line
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
		y+=(aim*cont)
	elif line[0] == 'd':
		aim+=cont
	elif line[0] == 'u':
		aim-=cont
	else:
		assert 0, oline
print(x, y)
print(x*y)

