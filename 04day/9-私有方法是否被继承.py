class Father():
	def __init__(self):
		self.__girl_count = 4 #处过个对象

	def getGirlCount(self):
		return self.__girl_count

	def makemoney(self):
		print("我会挣钱")

	def eat(self):
		print("会吃饭")

	def __girl(self):#私有方法
		print("处对象的大全")

	def askGirl(self):
		self.__girl()

class Son(Father):
	pass


xiaoming = Son()
xiaoming.makemoney()
xiaoming.eat()	
#xiaoming.__girl() 私有方法不会被继承
xiaoming.askGirl()
print(xiaoming.getGirlCount())
#print(xiaoming.__girl_count)私有属性不能被继承
	


	
	












