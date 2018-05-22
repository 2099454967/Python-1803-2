class Animal(object):

	def move(self):
		print("走")



class Dog(Animal):
		
	def move(self):
		print("狗四条腿走路")


class Person(Animal):
		
	def move(self):
		print("人用两条腿走路")




def walk(obj):
	obj.move()



dog = Dog()
walk(dog)

person = Person()
walk(person)	
