#!/usr/bin/env python3
import re

with open("input_4.txt") as f:
	lines=f.read()

passports = lines.split('\n\n')
cnt = 0
for entry in passports:
	score = 0
	fields = entry.split()
	if (len(fields) == 8) or ((len(fields) == 7) and (len(list(filter(lambda x: "cid" in x, fields))) == 0)): 
		byr = re.split(":", ''.join(list(filter(lambda x: "byr" in x, fields))))
		if (len(byr[1]) == 4) and (int(byr[1]) >= 1920) and (int(byr[1]) <= 2002):
			score += 1
		print(byr)
		iyr = re.split(":", ''.join(list(filter(lambda x: "iyr" in x, fields))))
		if (len(iyr[1]) == 4) and (int(iyr[1]) >= 2010) and (int(iyr[1]) <= 2020):
			score += 1
		print(iyr)
		eyr = re.split(":", ''.join(list(filter(lambda x: "eyr" in x, fields))))
		if (len(eyr[1]) == 4) and (int(eyr[1]) >= 2020) and (int(eyr[1]) <= 2030):
			score += 1
		print(eyr)
		hgt = re.split(":", ''.join(list(filter(lambda x: "hgt" in x, fields))))
		if re.search("cm", hgt[1]):
			tmp = re.split("cm", hgt[1])
			if (int(tmp[0]) >= 150) and (int(tmp[0]) <= 193):
				score+=1
		elif re.search("in", hgt[1]):
			tmp = re.split("in", hgt[1])
			if (int(tmp[0]) >= 59) and (int(tmp[0]) <= 76):
				score+=1
		print(hgt)
		hcl = re.split(":", ''.join(list(filter(lambda x: "hcl" in x, fields))))
		if (re.search("^\#[A-z,0-9]{6}$", hcl[1])):
			score += 1
		print(hcl)
		ecl = re.split(":", ''.join(list(filter(lambda x: "ecl" in x, fields))))
		approved_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if ecl[1] in approved_ecl:
			score += 1
		print(ecl)			
		pid = re.split(":", ''.join(list(filter(lambda x: "pid" in x, fields))))
		if re.search("^[0-9]{9}$", pid[1]):
			score += 1
	print(score)
	if (score == 7):
		cnt += 1
print("Valid passports: %d" % cnt)
