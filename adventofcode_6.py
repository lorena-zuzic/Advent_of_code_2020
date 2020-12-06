#!/usr/bin/env python3
import re
lines=open("input_6.txt", "r").read()
lines=re.split("\n\n", lines)
suma = 0
for group in lines:
    group = set(group)
    group.discard('\n')
    suma += len(group)
    
print(suma)
