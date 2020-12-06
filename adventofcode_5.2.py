#!/usr/bin/env python3

def placeread(boarding_pass):
    boarding_pass = boarding_pass.replace("F", "0")
    boarding_pass = boarding_pass.replace("B", "1")
    boarding_pass = boarding_pass.replace("L", "0")
    boarding_pass = boarding_pass.replace("R", "1")
    boarding_pass = int(boarding_pass, 2)
    return(boarding_pass)

f = open("input_5.txt", "r")
allseats = []
for line in f:
    seat = placeread(line)
    allseats.append(seat)
planeseats = set(range(min(allseats), (max(allseats)+1)))
myseat = list(planeseats - set(allseats))
print(myseat[0])
