class Person():
	
	def __init__(self):
		self.__money = 100#私有属性

	#下面这个方法就是解决不能直接通过xiaoming.__money的作用
	def getMoney(self):
		return self.__money

	def setMoney(self,money):
		if money <= 0:
			print("传入金额非法")
		else:
			self.__money = money
xiaoming = Person(10)
#xiaoming.__money = -100
xiaoming.setMoney(20)
print(xiaoming.getMoney())
#xiaoming.__money
