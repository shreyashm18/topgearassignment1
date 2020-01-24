lst=[4,5,7,1,2,9,6,3,8,0]
for i in lst:
	print(i)
print(f'slicing : {lst[1:10:2]}')
lst2=[15,52,44,18]
print(f'list concatenation: {lst+lst2}')
'''or can also use following method
lst.extend(lst2)
print(lst)'''
print(f'list repetetion : {lst*3}')

