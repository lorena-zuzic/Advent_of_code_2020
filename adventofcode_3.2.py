#!/usr/bin/env python3
import numpy as np
#f=open("test.txt", "r")
right=[1,3,5,7,1]
down=[1,1,1,1,2]
cnt_lst=[]
hpos=0
for i in range(len(right)):
	cnt=0
	nlines=0
	hpos=0
	f=open("input_3.txt", "r")
	for line in f.readlines():
		nlines += 1
		if (nlines % down[i] != 0) or (down[i] == 1):
			line=line.strip()
			if line[hpos] == "#":
				cnt += 1	
			hpos += right[i]
			if hpos >= len(line):
				hpos = hpos - len(line)
	cnt_lst.append(cnt)
mult = np.prod(cnt_lst)
print(cnt_lst)
print(mult)
