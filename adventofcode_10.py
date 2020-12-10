#!/usr/bin/env python3

f=open("input_10.txt", "r").read().split('\n')
lines=[int(f[i]) for i in range(len(f)-1)]

all_adapters=set(lines)
adaptersinbag=True
previous_adapter=0
diff=[]

while adaptersinbag:
	diff.append(min(all_adapters)-previous_adapter)
	previous_adapter = min(all_adapters)
	all_adapters = all_adapters - set([min(all_adapters)])
	print(all_adapters)
	if len(all_adapters)==0:
		adaptersinbag=False
		diff.append(3)

print(diff.count(1)* diff.count(3))
