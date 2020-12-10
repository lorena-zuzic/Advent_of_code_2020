#!/usr/bin/env python3

f=open("input_10.txt", "r").read().split('\n')
lines=[int(f[i]) for i in range(len(f)-1)]

all_adapters=set(lines)
adaptersinbag=True
previous_adapter=0
diff=[]
res=[0]
while adaptersinbag:
	diff.append(min(all_adapters)-previous_adapter)
	previous_adapter = min(all_adapters)
	res.append(min(all_adapters))
	all_adapters = all_adapters - set([min(all_adapters)])
	if len(all_adapters)==0:
		adaptersinbag=False
		diff.append(3)
		res.append(previous_adapter+3)

#print(diff.count(1)* diff.count(3))
print(res)
relevant_list=[]

tosave=[]
for i in range(1,len(res)-1):
	if res[i]==res[i-1]+1 and res[i]==res[i+1]-1:
		tosave.append(res[i])
	elif (res[i]!=res[i-1]+1 or res[i]!=res[i+1]-1) and len(tosave)>0:
		relevant_list.append(tosave)
		tosave=[]
print(relevant_list)


final = 1
for groups in relevant_list:
	if len(groups)==3:
		modif = 2**(len(groups)) - 1
		final=final*modif
	else:
		final=final * 2 ** len(groups)

print(final)
