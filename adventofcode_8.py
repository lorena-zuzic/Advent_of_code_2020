#!/usr/bin/env python3

f=open("test_8_2.txt", "r")
lines=f.readlines()
lines=[x.split() for x in lines]

unique_elements=True
pos = 0
acc_count = 0
used_pos = set(range(len(lines)))
print(used_pos)
while unique_elements:
	if lines[pos][0] == "nop":
		print("nop")
		test = used_pos & set([pos])
		type(test)
		if len(test) != 0:	
			used_pos = used_pos - set([pos])
		else:
			unique_elements = False
		pos += 1
	if lines[pos][0] == "jmp":
		print("jmp")
		test = used_pos & set([pos])
		if len(test) != 0:	
			used_pos = used_pos - set([pos])
		else:
			unique_elements = False
		pos = pos + int(lines[pos][1])
	if lines[pos][0] == "acc":
		print("acc")
		test = used_pos & set([pos])
		if len(test) != 0:	
			used_pos = used_pos - set([pos])
		else:
			unique_elements = False
			break
		acc_count += int(lines[pos][1])
		pos += 1
print(acc_count)

