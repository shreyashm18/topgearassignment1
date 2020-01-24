from math import ceil
prime=True
no=int(input('enter no\n'))
if(no==0 or no==1):
	print(f'{no} is not prime')
elif(no==2):
	print(f'{no} is prime')
else:
	for i in range(2,ceil(no/2)):
		if(no%i==0):
			#print(f'{no}%{i}={no%i}')
			prime=False
			break
if(prime):
	print(f'{no} is prime')
else:
	print(f'{no} is not prime')
