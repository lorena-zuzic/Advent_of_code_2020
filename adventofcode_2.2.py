#!/usr/bin/env python3
import re

f=open("input_2.txt", "r")
valid = 0
for line in f:
	pwd = re.split('[\s:-]', line)
	while '' in pwd:
		pwd.remove('')
	cnt = pwd[3].count(pwd[2])
	if (cnt >= int(pwd[0])) and (cnt <= int(pwd[1])):
		valid += 1
print(valid)
