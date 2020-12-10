#!/usr/bin/env python3
import copy 

f=open("input_8.txt", "r")
lines=f.readlines()
lines=[x.split() for x in lines]
fixed_lines = list(lines)
score = False

for i in range(len(fixed_lines)):
	lines = copy.deepcopy(fixed_lines)
	acc_count = 0
	pos = 0
	unique_elements = True
	used_pos = set(range(len(lines)))
	if fixed_lines[i][0] == "jmp":
		lines[i][0] = "nop"
	elif fixed_lines[i][0] == "nop":
		lines[i][0] = "jmp"
	while unique_elements:
		if pos >= (len(lines)-1):
			print(acc_count)
			print("we have a winner")
			unique_elements = False
			score = True
			break
		else:
			if lines[pos][0] == "nop":
				#print("nop")
				test = used_pos & set([pos])
				if len(test) != 0:	
					used_pos = used_pos - set([pos])
				else:
					unique_elements = False
					print("Try %d died" % i)
				pos += 1
			if lines[pos][0] == "jmp":
				#print("jmp")
				test = used_pos & set([pos])
				if len(test) != 0:	
					used_pos = used_pos - set([pos])
				else:
					unique_elements = False
					print("Try %d died" % i)
				pos = pos + int(lines[pos][1])
			if lines[pos][0] == "acc":
				#print("acc")
				test = used_pos & set([pos])
				if len(test) != 0:	
					used_pos = used_pos - set([pos])
				else:
					unique_elements = False
					print("Try %d died" % i)
					break
				acc_count += int(lines[pos][1])
				pos += 1

	if score:
		break


