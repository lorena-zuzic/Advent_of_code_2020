#!/usr/bin/env python3
import re

with open("input_4.txt") as f:
	lines=f.read()

passports = lines.split('\n\n')
cnt = 0
for entry in passports:
	fields = entry.split()
	if (len(fields) == 8) or ((len(fields) == 7) and (len(list(filter(lambda x: "cid" in x, fields))) == 0)): 
		cnt += 1
	else:
		print("Invalid")
		print(fields)

print(cnt)
