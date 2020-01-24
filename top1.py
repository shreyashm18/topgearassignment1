no1=int(input('enter 1st no\n'))
no2=int(input('enter 2nd no\n'))
operation=int(input('enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division'))
if(operation==1):
	print(f'{no1} + {no2} = {no1+no2}')
elif(operation==2):
	print(f'{no1} - {no2} = {no1-no2}')
elif(operation==3):
	print(f'{no1} * {no2} = {no1*no2}')
elif(operation==4):
	print(f'{no1} / {no2} = {no1/no2}')
else:print('invalid operation')