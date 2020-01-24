n=int(input('number till what u want fibonacci series'))
fst,snd=0,1
lst=[]
lst.append(fst)
def fib(a,b):
	lst.append(b)
	a,b=b,a+b
	return a,b
while(snd<=n):
	fst,snd=fib(fst,snd)
print(lst)