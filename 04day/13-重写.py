class Animal():

	def eat(self):
		print("吃")



class Dog(Animal):	
	#重写
	def eat(self):
		print("狗吃骨头")

	def wark(self):
		print("汪汪叫")


class xtq(Dog):
	#重写	
	def wark(self):
		print("嗷嗷叫")
		#第一种
		#Dog.wark(self)#调用父类的方法
		#第二种
		super().wark()

class Cat(Animal):
	def eat(self):
		print("猫吃耗子")


taidi = Dog()
taidi.eat()
xiaotq = xtq()
xiaotq.wark()
