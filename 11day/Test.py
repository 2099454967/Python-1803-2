def fib():
	i = 0
	a,b = 0,1
	while i < 8:
		#print(b)
		print("------haha------")
		temp = yield b
		print(temp)
		print("----hehe-----")
		a,b = b,a+b
		i+=1

