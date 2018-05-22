class Cow(object):
	__instance = None
	__init_flag = False
	def __init__(self,name):
		if Cow.__init_flag == False:
			self.name = name
			Cow.__init_flag=True
		

	def __new__(cls,name):

		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

cow = Cow("xiaowang")
cow1 = Cow("laowang")
print(cow.name)
print(id(cow))

print(cow1.name)
print(id(cow1))


		





