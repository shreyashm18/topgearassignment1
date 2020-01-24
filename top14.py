ent=int(input('how many entries?\t'))
print("enter employee names:\n")
#emp=['sm','ot','pk','aa','bb','cc','ff','ww','jj','rr']
#empid=[18,25,1,54,63,78,41,56,58,77]
emp=[]
empid=[]
for i in range(1,ent+1):
	emp.append(input(f"enter no {i} employee name:\n"))
	empid.append(int(input(f"enter {emp[i-1]}'s employee id:\n")))
print(emp,empid)
print(f'a. All emp info: {list(zip(emp,empid))}')
index=int(input('give idex'))
print(f'b. emp name: {emp[index]} emp id: {empid[index]}')
print(f'\nc. {emp[3:9]}')
print(f'\nd. {emp[2:]}')
times=int(input('e. how many times you want to repeat the elements?'))
print(f'\nlist repeated by {times}: {emp*times}\n {empid*times}')
print(f'\nf. concatenation of 2 lists: {emp+empid}\n')
print('g. :')
for i in range(len(emp)):
	print(f'\n{emp[i]} {empid[i]}')