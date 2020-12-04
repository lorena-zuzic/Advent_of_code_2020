#!/usr/bin/env python3

f=open("input_1.txt", "r")
filelines = f.readlines()
for line in filelines:
	for line2 in filelines:
		for line3 in filelines:
			suma=int(line)+int(line2)+int(line3)
			#print(suma)
			if (suma == 2020):
				mult=int(line)*int(line2)*int(line3)
				print(mult)

