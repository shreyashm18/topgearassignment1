lst=[]
print('enter 5 names \n')
for i in range(5):
	lst.append(input())
print(lst)
nm=input('enter name you want to search in list\t')
if nm in lst:
	print(f'{nm} is present in list')
else:
	print(f'{nm} not present')
status=False
for i in lst:
	if i==nm:
		status=True
		break
if status:
	print(f'{nm} is present in list')
else:
	print(f'{nm} not present')
print(f'\n element of list in reverse direction:\n')
for i in reversed(lst):
	print(i)