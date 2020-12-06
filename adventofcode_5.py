#/usr/bin/env python3

def placeread(boarding_pass):
    boarding_pass = boarding_pass.replace("F", "0")
    boarding_pass = boarding_pass.replace("B", "1")
    boarding_pass = boarding_pass.replace("L", "0")
    boarding_pass = boarding_pass.replace("R", "1")
    boarding_pass = int(boarding_pass, 2)
    return(boarding_pass)

f = open("input_5.txt", "r")
allsums = []
for line in f:
    sums = placeread(line[:7])*8 + placeread(line[7:])
    allsums.append(sums)
print(max(allsums))
