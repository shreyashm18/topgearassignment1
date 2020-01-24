import sys
if(len(sys.argv)==6):
	for i in range(1,len(sys.argv)):
		print(sys.argv[i])
elif(len(sys.argv)==4):
	if(sys.argv[1]==sys.argv[2]==sys.argv[3]):
		print(f'all are same')
	else:
		if(sys.argv[1]>=sys.argv[2] and sys.argv[1]>=sys.argv[3]):
			print(f'{sys.argv[1]} is biggest')
		elif(sys.argv[2]>=sys.argv[1] and sys.argv[2]>=sys.argv[3]):
			print(f'{sys.argv[2]} is biggest')
		elif(sys.argv[3]>=sys.argv[1] and sys.argv[3]>=sys.argv[2]):
			print(f'{sys.argv[3]} is biggest')
