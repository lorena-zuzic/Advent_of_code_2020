#!/usr/bin/env python3
import re
lines=open("input_6.txt", "r").read()
lines=re.split("\n\n", lines)
suma = 0
for group in lines:
    print("Group:\n%s" % group)
    group = group.split()
    inters = group[0]
    for person in group:
        inters = set(inters) & set(person)
    suma += len(inters)

print(suma)
