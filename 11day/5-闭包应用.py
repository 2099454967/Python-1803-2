def line_conf(a,b):
	def line(x):
		return a*x+b

	return line


f = line_conf(5,6)
print(f(1))
print(f(2))

f1 = line_conf(2,3)
f1(2)
f1(3)


def test1(a,b,x):
	return a*x+b


test1(2,3,1)
test1(2,3,2)



