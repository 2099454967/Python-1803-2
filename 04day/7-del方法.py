class Dog():

	#创建实例的对象的时候自动调用	
	def __init__(self):
		pass

	#打印实例的时候被调用 有返回值
	def __str__(self):

		return ""
	#del删除对象的时候被调用
	def __del__(self):
		print("del方法执行了")


taidi = Dog()#创建实例对象

hashiqi = taidi

del taidi
del hashiqi
print("程序结束了")


	
