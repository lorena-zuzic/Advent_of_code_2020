#!/usr/bin/env python3

f=open("input_3.txt", "r")
hpos=0
cnt=0
for line in f.readlines():
	line=line.strip()
	if line[hpos] == "#":
		cnt += 1	
	hpos += 3
	if hpos >= len(line):
		hpos = hpos - len(line)
print(cnt)
