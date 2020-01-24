no=int(input('enter to to check prime of not'))
status=False

def checkPrime(no):	
	st=False
	for i in range(2,int(no/2)+1):
		if no%i==0:
			st=True
			break
	return st
if(no==0 or no==1):
	status=True
else:
	status=checkPrime(no)
if not status:
	print(f'{no} is prime')
else:
	print(f'{no} is not prime')

N=int(input('enter till what u wanna generate prime nos?'))
primeno=[2]
for i in range(3,N+1):
	status=checkPrime(i)
	if not status:
		primeno.append(i)

print(primeno)