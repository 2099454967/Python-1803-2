class Dog():

	def __init__(self,age):
		self.age = age


	def wark(self):
		print("汪汪叫")

	def __str__(self):
		return "狗的年龄是%d"%self.age


xiaohuang = Dog(10)
print(xiaohuang)
xiaohuang.wark()
