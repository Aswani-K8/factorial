def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
n=int(input('enter the number:\n'))
if n==0:
	print('The factorial of 0 is 1')
else:
	print(fact(n))