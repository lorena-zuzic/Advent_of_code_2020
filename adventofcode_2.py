#!/usr/bin/env python3
import re

f=open("input_2.txt", "r")
valid = 0
for line in f:
	pwd = re.split('[\s:-]', line)
	while '' in pwd:
		pwd.remove('')
	if (pwd[3][int(pwd[0])-1] == pwd[2]) ^ (pwd[3][int(pwd[1])-1] == pwd[2]):
		valid += 1
print(valid)
