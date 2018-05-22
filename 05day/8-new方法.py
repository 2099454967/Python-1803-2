class Dog(object):

	def __init__(self):
		print("init方法")

	def __str__(self):
		print("str纺股份")
		return "对象描述信息"
	
	def __del__(self):
		print("del方法")
	
	def __new__(cls):#创建对象的作用
		print("new方法")
		return object.__new__(cls)
	

dog = Dog()	
print(id(dog))
