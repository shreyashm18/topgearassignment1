inp=int(input('how much numbers:\n'))
lst=[]
print(f'enter {inp} numbers\n')
for i in range(inp):
	lst.append(int(input()))
print(lst)
newlst=sorted(lst)
#print(newlst)
print(f'smallest no is {newlst[0]} and biggest no is {newlst[len(newlst)-1]}')