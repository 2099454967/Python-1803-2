class Dog(object):
	flag = 0	
	obj = None
	def __new__(cls):
		print(cls.flag)
		if cls.flag == 1:
			return cls.obj
		else:
			cls.flag = 1
			cls.obj = object.__new__(cls)
			return cls.obj
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
dog4 = Dog()
dog5 = Dog()

print(id(dog1))
print(id(dog2))
print(id(dog3))
print(id(dog4))
print(id(dog5))
print(id(dog2))
