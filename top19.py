lst=[n for n in range(1,101)]
for i in lst:
	if i%2==0:
		print(f'{i}\n')
print('\nusing for loop\n')
for i in lst:
	if i==50:
		break
	elif(i==10 or i==20 or i==30 or i==40):
		print('\n')
		continue
	else:
		print(i)
cnt=1
print('\nusing while loop\n')
while(cnt<=100):
	if lst[cnt-1]==90:
		break
	elif(lst[cnt-1]==60 or lst[cnt-1]==70 or lst[cnt-1]==80 or lst[cnt-1]==90):
		cnt+=1
		print('\n')
		continue
	else:
		print(lst[cnt-1])
		cnt+=1	