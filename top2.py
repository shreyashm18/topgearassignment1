
n1=int(input("1st no\n"))
n2=int(input("2nd no\n"))
n3=int(input("3rd no\n"))

if(n1==n2==n3):
	print(f'all are same')
else:
	
	if(n1>=n2 and n1>=n3):
		print(f'{n1} is biggest')
	elif(n2>=n1 and n2>=n3):
		print(f'{n2} is biggest')
	elif(n3>=n1 and n3>=n2):
		print(f'{n3} is biggest')