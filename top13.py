inp=input('enter numbers and press enter after every input(when u entered all numbers press enter 2 times)')
lst=[]
while inp:
	lst.append(int(inp))
	inp=input()
print(lst)
#sortedlist=sorted(lst)
#print(f'biggest no is {sortedlist[-1]}')
big=lst[0]
for i in lst:
	if i>big:
		big=i
print(f'biggest is {big}')