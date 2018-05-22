class Dog():
	count = 0#类属性
	def __init__(self,name):
		self.name = name
		#global count
		Dog.count+=1
		print(Dog.count)
"""
全局变量
count = 0
taidi  = Dog("泰迪")
count+=1
hashiqi = Dog("哈士奇")	
count+=1
print(count)
"""	

taidi = Dog("泰迪")
hanshiqi = Dog("哈士奇")
