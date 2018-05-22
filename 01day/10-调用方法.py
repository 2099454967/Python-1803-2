class Dog:
	#属性
	#行为
	def wangwang(self):#方法
		print("汪汪叫")
	def eat(self):
		print("狗吃骨头")

class Person:
	#属性
	#行为
	def eat(self):
		print("吃饭")
	
	def walk(self):
		print("人在走")

hashiqi = Dog()
hashiqi.wangwang()
hashiqi.eat()

limingrui = Person()
limingrui.eat()
limingrui.walk()
