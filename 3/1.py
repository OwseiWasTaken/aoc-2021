#! /bin/python3.10
lines:list[str] = []
with open("i") as f:
	lines = f.readlines()

linelen = len(lines[0])-1
bits = [
	0
]*linelen
#bitss = [
#	""
#]*linelen
# 12 bits in 1 line
for i in range(len(lines)):
	ln = lines[i][:-1]
	for j in range(len(ln)):
		char = ln[j]
		#bitss[j]+=char
		bits[j] += 1 * (-1 if char == '0' else 1)

#for bit in bitss:
#	z = bit.count('0') # zeros
#	o = bit.count('1') # ones
#	if z > o:
#		print('zero')
#	else:
#		print('one')
gamma = ""
epsilon = ""
for bit in bits:
	gamma += ('1' if bit > 0 else '0')
	epsilon += ('0' if bit > 0 else '1')

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma)
print(epsilon)
print(gamma*epsilon)

