class A():
	def testA(self):
		print("-------A------")

class B():
	
	def testB(self):
		print("-------B------")


class C(A,B):
	pass


c = C()

c.testA()
c.testB()


