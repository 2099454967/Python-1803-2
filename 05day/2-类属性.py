class Dog():
	count = 1#类属性
	def __init__(self,name):
		self.name = name#实例属性
		Dog.count +=1		

	def wark(self):
		print("汪汪叫")#实例方法

	@classmethod
	def test(cls):
		print("这是类方法")

	@classmethod
	def change(cls):
		cls.count +=1
		#Dog.count +=1

taidi = Dog("泰迪")
print(taidi.name)
taidi.wark()
#如果想调用类方法，可以通过类去直接调用或者通过类实例化出的对象也可调用
Dog.test()
taidi.test()

Dog.change()
#调用类属性,可以通过类直接调用或者通过类实例化出的对象也可以调用
print(Dog.count)
print(taidi.count)
