#!/usr/bin/env python3
f=open("input_7.txt", "r")
lines=f.readlines()

def parse(string):
    children = []
    count = string.count("bag")
    string = string.split()
    for i in range(1,count):
        children.append(' '.join(string[(i*4+1):(i*4+3)]))
    parent = ' '.join(string[0:2])
    if 'other bags.' in children:
        children.remove('other bags.')
    d = {parent:children}
    return(d)

d = {}
for line in lines:
    d = {**d, **parse(line)}
#print(d)

match_bag = ["shiny gold"]
result_bag = []
bagsleft = True

while bagsleft:
    score = 0
    for one_match_bag in match_bag:
        for out_bag, in_bag in d.items():
            if one_match_bag in in_bag:
                result_bag.append(out_bag)
                match_bag.append(out_bag)
                score += 1
    match_bag = []
    if (score == 0):
        bagsleft = False

print(len(set(result_bag)))
print(set(result_bag))

