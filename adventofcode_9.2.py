#!/usr/bin/env python3

f=open("input_9.txt", "r")
lines = f.read().split('\n')
lines = [int(i) for i in lines[0:(len(lines)-1)]]

start = 25

for i in range(start,len(lines)):	
	nr = lines[i]
	res = 0
	for j in range(i-start,i):
		num1 = lines[j]
		for k in range(i-start,i):
			num2 = lines[k]
			if nr == num1+num2:
				res = int(nr)	
				break
		else:
			continue
		break
	if res == 0:
		print("No sum is %d" % nr)
		error_number = int(nr)
		break
print(error_number)
result = None
for i in range(len(lines)):
	contiguous = []
	for j in range(i,len(lines)):
		contiguous.append(lines[j])
		if sum(contiguous) > error_number:
			break	
		elif sum(contiguous) == error_number:
			result = min(contiguous)+max(contiguous)
			print("Result is: %d" % result)
			break
	if result is not None:
		break
