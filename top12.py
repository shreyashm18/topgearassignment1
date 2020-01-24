numbers=input("enter 10 numbers, give space between every no and press enter when you are done")
lst=[]
lst1=numbers.split(' ')
for i in lst1:
	lst.append(int(i))
print(lst)
print(lst1)
avg=sum(lst)/len(lst)
print(f'average = {avg}')
less=[]
more=[]
avgno=[]
for i in lst:
	if i<avg:
		less.append(i)
	elif i>avg:
		more.append(i)
	else:
		avgno.append(i)
print(f'no less that average: \t {less} and total no are {len(less)}')
print(f'no more that average: \t {more} and total no are {len(more)}')
print(f'no equal to average: \t {avgno} and total no are {len(avgno)}')